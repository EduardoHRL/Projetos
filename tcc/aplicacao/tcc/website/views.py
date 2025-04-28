from .models import *
from .forms import *
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib.auth.hashers import make_password
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from django.views.decorators.cache import never_cache
from django.utils.decorators import method_decorator
from datetime import datetime, timedelta
from .filters import *
from django_filters.views import FilterView
import requests

def admin_check(user):
    return user.is_authenticated and (user.is_staff or user.is_superuser)
admin_required = user_passes_test(admin_check)

@login_required
@never_cache
def index(request):
    return render(request, 'index.html')

# Views da agenda
@login_required
@never_cache
def agenda(request):
    return render(request, 'agenda/agenda.html')

@require_GET
def reservas_json(request):
    todas_reservas = Reservas.objects.all()
    out = []
    for reserva in todas_reservas:
        out.append({
            'title': reserva.laboratorio.lab_nome,
            'start': reserva.res_inicio.isoformat(),
            'end': reserva.res_fim.isoformat(),
            'responsavel': reserva.professor.username,
            'motivo': reserva.res_descricao
        })
    
    return JsonResponse(out, safe=False)

# Views de Login e Cadastro
@never_cache
def logar(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        user = authenticate(request, email=email, password=senha)
        
        if user:
            login(request, user)
            response = redirect('index')
        
            if request.POST.get('remeberMe'):
                response.set_cookie(
                    'rememberMe'
                    '1',
                    max_age=30*24*60*60,
                    httponly=True,
                    secure=True,
                    samesite='Lax'
                )
            return response
        else:
            messages.error(request, 'Email e/ou senha estão incorretos')
    
    return render(request, 'login.html')

@never_cache
def cadastro(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        cpf = request.POST.get('cpf')
        telefone = request.POST.get('telefone')
        tipoUsuario = request.POST.get('tipoUsuario')
        senha = request.POST.get('senha')

        if Usuarios.objects.filter(email=email).exists() or Usuarios.objects.filter(cpf=cpf).exists():
            if Usuarios.objects.filter(email=email).exists():
                messages.error(request, 'Email já existe.')
            if Usuarios.objects.filter(cpf=cpf).exists():
                messages.error(request, 'Cpf já existe.')
            return redirect('cadastro')
        
        if tipoUsuario == 'admin':
            usuarios = Usuarios.objects.create(
                username = nome,
                email = email,
                cpf = cpf,
                telefone = telefone,
                is_superuser = True,
                password = make_password(senha)
        )
        elif tipoUsuario == 'usuario':
                usuarios = Usuarios.objects.create(
                username = nome,
                email = email,
                cpf = cpf,
                telefone = telefone,
                is_superuser = False,
                password = make_password(senha),
                is_active = False
            )
        messages.success(request, 'Cadastro realizado com sucesso')
        return HttpResponseRedirect(reverse('login'))

    return render(request, 'cadastro.html')

@login_required
@require_http_methods(["POST"])
@never_cache
def sair(request):
    logout(request)
    response = redirect('login')
    response.delete_cookie('rememberMe')
    response['Cache-Control'] = 'no-store, must-revalidate'
    return response

# Views dos Usuários
@method_decorator(admin_required, name='dispatch')
@method_decorator(never_cache, name='dispatch')
class UsuariosListView(LoginRequiredMixin, ListView):
    template_name = 'professores/lista_usuarios.html'
    model = Usuarios
    context_object_name = 'usuarios'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['solicitacoes'] = Usuarios.objects.filter(is_active = False)
        return context
    
def aprovar_usuario(request, user_id):
    if request.user.is_staff or request.user.is_superuser:
        usuario = Usuarios.objects.get(id=user_id)
        usuario.is_active = True
        usuario.save()
    return redirect('lista_usuarios')

def rejeitar_usuario(request, user_id):
    if request.user.is_staff or request.user.is_superuser:
        usuario = Usuarios.objects.get(id=user_id)
        usuario.delete()
    return redirect('lista_usuarios')

@require_POST
@login_required
@never_cache
def atualiza_usuarios(request, pk):
    user = get_object_or_404(Usuarios, pk=pk)

    user.username = request.POST.get('username')
    user.email = request.POST.get('email')
    user.telefone = request.POST.get('telefone')

    if request.user != user:
        is_superuser = request.POST.get('is_superuser')
        user.is_superuser = True if is_superuser == '1' else False

    user.save()
    messages.success(request, 'Usuário atualizado com sucesso.')
    return redirect('lista_usuarios')


@require_POST
@login_required
@never_cache
def excluir_usuario(request, pk):
    user = get_object_or_404(Usuarios, pk=pk)

    if request.user == user:
        messages.error(request, 'Você não pode excluir a si mesmo.')
    else:
        user.delete()
        messages.success(request, 'Usuário excluído com sucesso.')

    return redirect('lista_usuarios')

# Views dos Laboratórios
@method_decorator(never_cache, name='dispatch')
class LaboratoriosListView(LoginRequiredMixin, FilterView):
    template_name = 'laboratorios/lista_laboratorios.html'
    model = Laboratorios
    context_object_name = 'laboratorios'
    filterset_class = LaboratorioFilter

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reserva'] = Reservas.objects.all()
        return context
        
@method_decorator(admin_required, name='dispatch')
@method_decorator(never_cache, name='dispatch')
class AdminLaboratoriosListView(LoginRequiredMixin, ListView):
    template_name = 'laboratorios/admin/lista_laboratorios.html'
    model = Laboratorios
    context_object_name = 'laboratorios'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = LaboratoriosForm
        context['reserva'] = Reservas.objects.all()
        return context
    
@method_decorator(admin_required, name='dispatch')
@method_decorator(never_cache, name='dispatch')
class LaboratoriosCreateView(LoginRequiredMixin, CreateView):
    template_name = 'laboratorios/admin/cadastro_laboratorios.html'
    model = Laboratorios
    form_class = LaboratoriosForm

    def form_valid(self, form):
        self.object = form.save()

        equipamentos = self.request.POST.getlist('equipamentos[]')
        quantidades = self.request.POST.getlist('quantidades[]')

        for nome, qtd in zip(equipamentos, quantidades):
            if nome.strip() == '' or not qtd:
                continue

            equipamento, _ = Equipamentos.objects.get_or_create(equip_nome=nome.strip())
            LaboratorioEquipamento.objects.create(
                laboratorio=self.object,
                equipamento=equipamento,
                quantidade=int(qtd)
            )

        return JsonResponse({
            'success': True,
            'lab_codigo': self.object.lab_codigo,
            'lab_nome': self.object.lab_nome,
            'lab_descricao': self.object.lab_descricao,
            'lab_capacidade': self.object.lab_capacidade,
            'lab_status': self.object.lab_status,
            'lab_foto': self.object.lab_foto.url if self.object.lab_foto else '',
        })

    def form_invalid(self, form):
        return JsonResponse({
            'success': False,
            'errors': form.errors.as_json()
        }, status=400)


@method_decorator(admin_required, name='dispatch')
@method_decorator(never_cache, name='dispatch')    
class LaboratoriosUpdateView(LoginRequiredMixin, UpdateView):
    model = Laboratorios
    form_class = LaboratoriosForm
    pk_url_kwarg = 'lab_codigo'

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.form_class(request.POST, request.FILES, instance=self.object)
        
        if form.is_valid():
            return self.form_valid(form)
        return self.form_invalid(form)

    def form_valid(self, form):
        try:
            self.object = form.save()
            
            LaboratorioEquipamento.objects.filter(laboratorio=self.object).delete()
            equipamentos = self.request.POST.getlist('equipamentos[]')
            quantidades = self.request.POST.getlist('quantidades[]')
            
            for nome, qtd in zip(equipamentos, quantidades):
                if nome.strip() and qtd:
                    equipamento, _ = Equipamentos.objects.get_or_create(equip_nome=nome.strip())
                    LaboratorioEquipamento.objects.create(
                        laboratorio=self.object,
                        equipamento=equipamento,
                        quantidade=int(qtd)
                    )
            
            return JsonResponse({
                'success': True,
                'message': 'Laboratório atualizado com sucesso!'
            })
            
        except Exception as e:
            return JsonResponse({
                'success': False,
                'message': f'Erro ao atualizar: {str(e)}'
            }, status=500)

    def form_invalid(self, form):
        return JsonResponse({
            'success': False,
            'errors': form.errors.get_json_data()
        }, status=400)

@method_decorator(admin_required, name='dispatch')
@method_decorator(never_cache, name='dispatch')    
class LaboratoriosDeleteView(LoginRequiredMixin, DeleteView):
    model = Laboratorios
    pk_url_kwarg = 'lab_codigo'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return JsonResponse({'success': True})


# Views das Reservas

@method_decorator(never_cache, name='dispatch')
class CriarReserva(LoginRequiredMixin, FormView):
    template_name = 'reservas/criar_reserva.html'
    model = Reservas
    form_class = ReservasForm
    success_url = reverse_lazy('lista_laboratorios')

    def form_valid(self, form):
        form.instance.professor = self.request.user
        reserva_base = form.save(commit=False)

        if reserva_base.res_repeticao == "S":
            return self._salvar_repeticoes(form, reserva_base)
        else:
            reserva_base.laboratorio.lab_status = 'usando'
            reserva_base.laboratorio.save()
            reserva_base.save()
            return super().form_valid(form)

    def _salvar_repeticoes(self, form, reserva_base):
        inicio = reserva_base.res_inicio
        fim = reserva_base.res_fim
        dias_semana = form.cleaned_data["res_dia_semana"]
        intervalo = form.cleaned_data["res_intervalo_semanas"]
        data_limite = form.cleaned_data["res_data_final_repeticao"]

        reservas_criadas = []

        dias_semana = [int(dia) for dia in dias_semana]
        data_atual = inicio.date()

        while data_atual <= data_limite:
            for dia in dias_semana:
                dia_reserva = self._proxima_data(data_atual, dia)

                if dia_reserva > data_limite:
                    continue

                dt_inicio = datetime.combine(dia_reserva, inicio.time())
                dt_fim = datetime.combine(dia_reserva, fim.time())

                reserva_base.laboratorio.lab_status = 'usando'
                reserva_base.laboratorio.save()

                nova_reserva = Reservas.objects.create(
                    professor=self.request.user,
                    laboratorio=reserva_base.laboratorio,
                    res_inicio=dt_inicio,
                    res_fim=dt_fim,
                    res_repeticao='N',
                    res_descricao=reserva_base.res_descricao,
                )
                reservas_criadas.append(nova_reserva)

            data_atual += timedelta(weeks=intervalo)

        return super().form_valid(form)

    def _proxima_data(self, data_base, dia_semana):
        dias_ate_dia = (dia_semana - data_base.weekday() + 7) % 7
        return data_base + timedelta(days=dias_ate_dia)

class AtualizarReserva(LoginRequiredMixin, UpdateView):
    template_name = 'reservas/atualizar.html'
    model = Reservas
    success_url = reverse_lazy('lista_laboratorios')
    form_class = AtualizarReservasForm
    pk_url_kwarg = 'res_codigo'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['laboratorios'] = Laboratorios.objects.all()
        return context

class ExcluirReserva(LoginRequiredMixin, DeleteView):
    model = Reservas
    success_url = reverse_lazy('lista_laboratorios')
    def post(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        lab = self.object.laboratorio
        lab.lab_status = 'disponivel'
        lab.save()

        return super().delete(request, *args, **kwargs)
    

# Views da escola

@method_decorator(never_cache, name='dispatch')
@method_decorator(admin_required, name='dispatch')
class EscolaUpdateView(UpdateView):
    model = Escola
    form_class = EscolaForm
    template_name = 'escola/atualizar_escola.html'
    context_object_name = 'escola'
    success_url = reverse_lazy('escola')

    def get_object(self, queryset=None):
        return Escola.objects.first()

    def form_valid(self, form):
        messages.success(self.request, 'Informações atualizadas com sucesso!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Erro ao salvar os dados.')
        return super().form_invalid(form)

def buscar_cep(request):
    if request.method == 'GET' and 'cep' in request.GET:
        cep = request.GET['cep'].replace('-', '')
        if len(cep) == 8:
            try:
                response = requests.get(f'https://viacep.com.br/ws/{cep}/json/', timeout=5)
                data = response.json()
                if 'erro' not in data:
                    return JsonResponse({
                        'bairro': data.get('bairro', ''),
                        'cidade': data.get('localidade', ''),
                        'estado': data.get('uf', '')
                    })
            except requests.RequestException:
                pass
    return JsonResponse({'error': 'CEP não encontrado'}, status=400)

@method_decorator(never_cache, name='dispatch')
class EscolaListView(LoginRequiredMixin, ListView):
    template_name = 'escola/escola.html'
    model = Escola
    context_object_name = 'escola'

    
