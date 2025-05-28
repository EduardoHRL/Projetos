from .models import *
from .forms import *
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import *
from django.contrib.auth import authenticate, login, logout, views as auth_views
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib.auth.hashers import make_password
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from django.views.decorators.cache import never_cache
from django.utils.decorators import method_decorator
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from .filters import *
from django_filters.views import FilterView
import requests
import json
from django.db.models import Q
from cpf_field.validators import validate_cpf,ValidationError
from django.utils import timezone

def admin_check(user):
    return user.is_authenticated and (user.is_staff or user.is_superuser)
admin_required = user_passes_test(admin_check)


@login_required
@never_cache
def historico_reservas(request):
    historicos = Reservas.history.select_related('laboratorio', 'professor')\
        .filter(res_repeticao_original__isnull=True)\
        .order_by('-history_date')
    return render(request, 'reservas/historico.html', {'historico': historicos})

@login_required
@never_cache
def historico_reservas_admin(request):
    historicos = Reservas.history.select_related('laboratorio', 'professor')\
        .filter(res_repeticao_original__isnull=True)\
        .order_by('-history_date')
    return render(request, 'historico.html', {'historico': historicos})

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
    # Inclui todas as reservas principais (não apenas as repetidas)
    todas_reservas = Reservas.objects.select_related('laboratorio', 'professor').filter(
        res_repeticao_original__isnull=True
    )
    
    out = []
    
    for reserva in todas_reservas:
        # Pega a primeira ocorrência da reserva (original)
        inicio = reserva.res_inicio
        fim = reserva.res_fim
        
        # Se for reserva recorrente, ajusta o fim para o mesmo dia
        if reserva.res_repeticao != 'N':
            fim = inicio + timedelta(
                hours=(reserva.res_fim - reserva.res_inicio).seconds // 3600
            )
        
        out.append({
            'id': reserva.res_codigo,
            'title': f"{reserva.laboratorio.lab_nome} - {reserva.professor.username}",
            'start': inicio.isoformat(),
            'end': fim.isoformat(),
            'description': reserva.res_descricao,
            'color': '#3b82f6',  # Cor azul para todas as reservas
            'textColor': '#ffffff',
            'borderColor': '#1d4ed8',
            'extendedProps': {
                'responsavel': reserva.professor.username,
                'laboratorio': reserva.laboratorio.lab_nome,
                'motivo': reserva.res_descricao,
                'status': reserva.res_status
            }
        })
        
        # Adiciona as repetições se existirem
        if reserva.repeticoes.exists():
            for repeticao in reserva.repeticoes.all():
                out.append({
                    'id': repeticao.res_codigo,
                    'title': f"{reserva.laboratorio.lab_nome} - {reserva.professor.username}",
                    'start': repeticao.res_inicio.isoformat(),
                    'end': repeticao.res_fim.isoformat(),
                    'color': '#93c5fd',  # Cor mais clara para repetições
                    'textColor': '#1e3a8a',
                    'borderColor': '#60a5fa',
                    'extendedProps': {
                        'responsavel': reserva.professor.username,
                        'laboratorio': reserva.laboratorio.lab_nome,
                        'motivo': reserva.res_descricao,
                        'status': reserva.res_status,
                        'repeticao': True
                    }
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
        senha = request.POST.get('senha')
        confirmarSenha = request.POST.get('confirmarSenha')
        try:
            validate_cpf(cpf)
        except ValidationError:
            messages.error(request, 'CPF inválido')
            return redirect('cadastro')

        if Usuarios.objects.filter(email=email).exists() or Usuarios.objects.filter(cpf=cpf).exists():
            if Usuarios.objects.filter(email=email).exists():
                messages.error(request, 'Email já existe.')
            if Usuarios.objects.filter(cpf=cpf).exists():
                messages.error(request, 'Cpf já existe.')
            return redirect('cadastro')
        
        if senha != confirmarSenha:
            messages.error(request, 'As duas senhas não coincidem.')
        
        
        usuarios = Usuarios.objects.create(
            username = nome,
            email = email,
            cpf = cpf,
            telefone = telefone,
            is_superuser = False,
            is_staff = False,
            is_active = False,
            password = make_password(senha)
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

DIAS_SEMANA = {
    '0': 'Segunda-feira',
    '1': 'Terça-feira',
    '2': 'Quarta-feira',
    '3': 'Quinta-feira',
    '4': 'Sexta-feira',
    '5': 'Sábado',
    '6': 'Domingo',
}

def horarios_laboratorio(request, lab_codigo):
    try:
        disponibilidades = Disponibilidade.objects.filter(laboratorio__lab_codigo=lab_codigo)
        horarios = []
        
        hoje = datetime.now().date()
        datas_exemplo = {
            '0': hoje + timedelta(days=(0 - hoje.weekday()) % 7),  # Segunda
            '1': hoje + timedelta(days=(1 - hoje.weekday()) % 7),  # Terça
            '2': hoje + timedelta(days=(2 - hoje.weekday()) % 7),  # Quarta
            '3': hoje + timedelta(days=(3 - hoje.weekday()) % 7),  # Quinta
            '4': hoje + timedelta(days=(4 - hoje.weekday()) % 7),  # Sexta
            '5': hoje + timedelta(days=(5 - hoje.weekday()) % 7),  # Sábado
            '6': hoje + timedelta(days=(6 - hoje.weekday()) % 7)   # Domingo
        }
        
        for disp in disponibilidades:
            dias = disp.hor_diasDisponiveis.split(',')
            for dia in dias:
                data_exemplo = datas_exemplo[dia]
                horarios.append({
                    'dias': dia,
                    'inicio': disp.hor_inicio.strftime('%H:%M'),
                    'fim': disp.hor_fim.strftime('%H:%M'),
                    'data_exemplo_inicio': f"{data_exemplo.isoformat()} {disp.hor_inicio.strftime('%H:%M')}",
                    'data_exemplo_fim': f"{data_exemplo.isoformat()} {disp.hor_fim.strftime('%H:%M')}"
                })
        
        return JsonResponse({'horarios': horarios})
    
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)
    
# Views dos Laboratórios
@method_decorator(never_cache, name='dispatch')
class LaboratoriosListView(LoginRequiredMixin, FilterView):
    template_name = 'laboratorios/lista_laboratorios.html'
    model = Laboratorios
    context_object_name = 'laboratorios'
    filterset_class = LaboratorioFilter

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        reservas = Reservas.objects.filter(res_repeticao_original__isnull=True)
        context['reserva'] = reservas

        professores_por_lab = {}
        for reserva in reservas:
            lab_id = reserva.laboratorio.lab_codigo
            professores_por_lab.setdefault(lab_id, [])
            professores_por_lab[lab_id].append(reserva.professor.username)

        professores_por_lab_json = {
            str(k): json.dumps(v) for k, v in professores_por_lab.items()
        }
        
        context['professores_por_lab'] = professores_por_lab_json

        for key in professores_por_lab:
            professores_por_lab[key] = list(set(professores_por_lab[key]))

        horarios = Disponibilidade.objects.all()
        for horario in horarios:
            dias_disponiveis = [DIAS_SEMANA[d] for d in horario.hor_diasDisponiveis.split(",")]
            horario.dias_formatados = ", ".join(dias_disponiveis)

        context['horarios'] = horarios

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
        context['reserva'] = Reservas.objects.filter(res_repeticao_original__isnull=True)
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
        dias_semana = self.request.POST.getlist('dias_semana[]')
        hor_inicio = self.request.POST.getlist('hor_inicio[]')
        hor_fim = self.request.POST.getlist('hor_fim[]')

        for nome, qtd in zip(equipamentos, quantidades):
            if nome.strip() == '' or not qtd:
                continue

            equipamento, _ = Equipamentos.objects.get_or_create(equip_nome=nome.strip())
            LaboratorioEquipamento.objects.create(
                laboratorio=self.object,
                equipamento=equipamento,
                quantidade=int(qtd)
            )
        
        for index in range(len(hor_inicio)):
            dias = self.request.POST.getlist(f'dias_semana_{index}[]')
            if dias and hor_inicio[index] and hor_fim[index]:
                Disponibilidade.objects.create(
                    laboratorio=self.object,
                    hor_inicio=hor_inicio[index],
                    hor_fim=hor_fim[index],
                    hor_diasDisponiveis=",".join(dias)
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

            Disponibilidade.objects.filter(laboratorio=self.object).delete()

            equipamentos = self.request.POST.getlist('equipamentos[]')
            quantidades = self.request.POST.getlist('quantidades[]')
            hor_inicio = self.request.POST.getlist('hor_inicio[]')
            hor_fim = self.request.POST.getlist('hor_fim[]')

            for nome, qtd in zip(equipamentos, quantidades):
                if nome.strip() and qtd:
                    equipamento, _ = Equipamentos.objects.get_or_create(equip_nome=nome.strip())
                    LaboratorioEquipamento.objects.create(
                        laboratorio=self.object,
                        equipamento=equipamento,
                        quantidade=int(qtd)
                    )

            for index in range(len(hor_inicio)):
                dias = self.request.POST.getlist(f'dias_semana_{index}[]')
                if dias and hor_inicio[index] and hor_fim[index]:
                    Disponibilidade.objects.create(
                        laboratorio=self.object,
                        hor_inicio=hor_inicio[index],
                        hor_fim=hor_fim[index],
                        hor_diasDisponiveis=",".join(dias)
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

@require_GET
def verificar_disponibilidade(request, lab_codigo):
    data = request.GET.get('data')
    hora_inicio = request.GET.get('hora_inicio')
    hora_fim = request.GET.get('hora_fim')
    
    try:
        data_obj = datetime.strptime(data, '%Y-%m-%d').date()
        inicio = datetime.strptime(f"{data} {hora_inicio}", '%Y-%m-%d %H:%M')
        fim = datetime.strptime(f"{data} {hora_fim}", '%Y-%m-%d %H:%M')
        
        # Verifica se há horário disponível para o horário solicitado
        disponivel = Disponibilidade.objects.filter(
            laboratorio__lab_codigo=lab_codigo,
            hor_inicio__lte=hora_inicio,
            hor_fim__gte=hora_fim
        ).exists()
        
        if not disponivel:
            return JsonResponse({
                'disponivel': False,
                'mensagem': 'Horário fora do período disponível para este laboratório'
            }, status=400)
        
        # Verifica conflitos com outras reservas
        conflitos = Reservas.objects.filter(
            laboratorio__lab_codigo=lab_codigo,
            res_inicio__lt=fim,
            res_fim__gt=inicio
        ).exists()
        
        if conflitos:
            return JsonResponse({
                'disponivel': False,
                'mensagem': 'Conflito com outra reserva existente'
            }, status=400)
        
        return JsonResponse({
            'disponivel': True,
            'mensagem': 'Horário disponível'
        })
        
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)
    
@require_GET
def horarios_disponiveis(request, lab_codigo):
    data = request.GET.get('data')
    try:
        data_obj = datetime.strptime(data, '%Y-%m-%d').date()
        
        # Obter todos os horários disponíveis para o laboratório
        disponibilidades = Disponibilidade.objects.filter(
            laboratorio__lab_codigo=lab_codigo
        )
        
        # Obter todas as reservas para a data
        reservas = Reservas.objects.filter(
            laboratorio__lab_codigo=lab_codigo,
            res_inicio__date=data_obj
        )
        
        horarios = []
        for disp in disponibilidades:
            horario_conflita = False
            for reserva in reservas:
                # Verificar se há sobreposição
                if (reserva.res_inicio.time() < disp.hor_fim and
                    reserva.res_fim.time() > disp.hor_inicio):
                    horario_conflita = True
                    break
            if not horario_conflita:
                horarios.append({
                    'inicio': disp.hor_inicio.strftime('%H:%M'),
                    'fim': disp.hor_fim.strftime('%H:%M'),
                    'dias_disponiveis': disp.hor_diasDisponiveis  # Mantido para referência, mas não usado na lógica
                })
        
        return JsonResponse({'horarios': horarios})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)

@method_decorator(never_cache, name='dispatch')
class CriarReserva(LoginRequiredMixin, FormView):
    template_name = 'reservas/criar_reserva.html'
    model = Reservas
    form_class = ReservasForm
    success_url = reverse_lazy('lista_laboratorios')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        lab_codigo = self.kwargs.get('lab_codigo')
        laboratorio = get_object_or_404(Laboratorios, lab_codigo=lab_codigo)
        context['laboratorio'] = laboratorio
        context['horarios_disponiveis'] = Disponibilidade.objects.filter(
            laboratorio=laboratorio
        )
        return context
    
    def form_valid(self, form):
        reserva = form.save(commit=False)
        reserva.professor = self.request.user

        inicio_str = reserva.res_inicio.strftime('%Y-%m-%d %H:%M:%S')
        fim_str = reserva.res_fim.strftime('%Y-%m-%d %H:%M:%S')
        
        reserva.res_inicio = timezone.make_aware(
            datetime.strptime(inicio_str, '%Y-%m-%d %H:%M:%S'),
            timezone.get_current_timezone()
        )
        reserva.res_fim = timezone.make_aware(
            datetime.strptime(fim_str, '%Y-%m-%d %H:%M:%S'),
            timezone.get_current_timezone()
        )
        
        if not self._horario_disponivel(reserva):
            form.add_error(None, "O horário selecionado não está disponível ou conflita com outra reserva")
            return self.form_invalid(form)
        
        form.instance.professor = self.request.user
        reserva_base = form.save(commit=False)
        tipo_repeticao = reserva_base.res_repeticao

        if tipo_repeticao == "S":
            return self._salvar_repeticoes_semanais(form, reserva_base)
        elif tipo_repeticao == "D":
            return self._salvar_repeticoes_diarias(form, reserva_base)
        elif tipo_repeticao == "M":
            return self._salvar_repeticoes_mensais(form, reserva_base)
        elif tipo_repeticao == "A":
            return self._salvar_repeticoes_anuais(form, reserva_base)
        else:
            reserva_base.laboratorio.lab_status = 'usando'
            reserva_base.laboratorio.save()
            reserva_base.save()
            return super().form_valid(form)

    def _horario_disponivel(self, reserva):
        hora_inicio = reserva.res_inicio.astimezone(timezone.get_current_timezone()).replace(second=0, microsecond=0).time()
        hora_fim = reserva.res_fim.astimezone(timezone.get_current_timezone()).replace(second=0, microsecond=0).time()

        print(f"🚩 Verificando disponibilidade para horário ({hora_inicio} até {hora_fim})")

        # Verifica se o horário está dentro de algum período de disponibilidade do laboratório
        disponibilidades = Disponibilidade.objects.filter(
            laboratorio=reserva.laboratorio,
            hor_inicio__lte=hora_inicio,
            hor_fim__gte=hora_fim
        )

        print(f"🚩 Disponibilidades encontradas: {disponibilidades}")

        if not disponibilidades.exists():
            print("❌ Nenhuma disponibilidade compatível encontrada.")
            return False

        # Verificar conflitos com outras reservas
        conflitos = Reservas.objects.filter(
            laboratorio=reserva.laboratorio,
            res_inicio__lt=reserva.res_fim,
            res_fim__gt=reserva.res_inicio
        ).exclude(pk=reserva.pk if reserva.pk else None)

        if conflitos.exists():
            print("❌ Conflito detectado com outra reserva.")
            return False

        print("✅ Horário está livre e disponível.")
        return True

    def _salvar_repeticoes_semanais(self, form, reserva_base):
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
                Reservas.objects.create(
                    professor=self.request.user,
                    laboratorio=reserva_base.laboratorio,
                    res_inicio=dt_inicio,
                    res_fim=dt_fim,
                    res_repeticao='S',
                    res_descricao=reserva_base.res_descricao,
                    res_repeticao_original=reserva_base
                )
            data_atual += timedelta(weeks=intervalo)
        return super().form_valid(form)

    def _salvar_repeticoes_diarias(self, form, reserva_base):
        inicio = reserva_base.res_inicio
        fim = reserva_base.res_fim
        data_limite = form.cleaned_data["res_data_final_repeticao"]
        data_atual = inicio

        reserva_base.laboratorio.lab_status = 'usando'
        reserva_base.laboratorio.save()
        reserva_base.save()

        while data_atual.date() <= data_limite:
            dt_inicio = datetime.combine(data_atual.date(), inicio.time())
            dt_fim = datetime.combine(data_atual.date(), fim.time())

            Reservas.objects.create(
                professor=self.request.user,
                laboratorio=reserva_base.laboratorio,
                res_inicio=dt_inicio,
                res_fim=dt_fim,
                res_repeticao='D',
                res_descricao=reserva_base.res_descricao,
                res_repeticao_original=reserva_base
            )
            data_atual += timedelta(days=1)
        return super().form_valid(form)

    def _salvar_repeticoes_mensais(self, form, reserva_base):
        inicio = reserva_base.res_inicio
        fim = reserva_base.res_fim
        data_limite = form.cleaned_data["res_data_final_repeticao"]
        data_atual = inicio

        while data_atual.date() <= data_limite:
            dt_inicio = datetime.combine(data_atual.date(), inicio.time())
            dt_fim = datetime.combine(data_atual.date(), fim.time())
            reserva_base.laboratorio.lab_status = 'usando'
            reserva_base.laboratorio.save()
            Reservas.objects.create(
                professor=self.request.user,
                laboratorio=reserva_base.laboratorio,
                res_inicio=dt_inicio,
                res_fim=dt_fim,
                res_repeticao='M',
                res_descricao=reserva_base.res_descricao,
                res_repeticao_original=reserva_base
            )
            data_atual += relativedelta(months=1)
        return super().form_valid(form)

    def _salvar_repeticoes_anuais(self, form, reserva_base):
        inicio = reserva_base.res_inicio
        fim = reserva_base.res_fim
        data_limite = form.cleaned_data["res_data_final_repeticao"]
        data_atual = inicio

        while data_atual.date() <= data_limite:
            dt_inicio = datetime.combine(data_atual.date(), inicio.time())
            dt_fim = datetime.combine(data_atual.date(), fim.time())
            reserva_base.laboratorio.lab_status = 'usando'
            reserva_base.laboratorio.save()
            Reservas.objects.create(
                professor=self.request.user,
                laboratorio=reserva_base.laboratorio,
                res_inicio=dt_inicio,
                res_fim=dt_fim,
                res_repeticao='A',
                res_descricao=reserva_base.res_descricao,
                res_repeticao_original=reserva_base
            )
            data_atual += relativedelta(years=1)
        return super().form_valid(form)

    def _proxima_data(self, data_base, dia_semana):
        dias_ate_dia = (dia_semana - data_base.weekday() + 7) % 7
        return data_base + timedelta(days=dias_ate_dia)


@method_decorator(never_cache, name='dispatch')
class AtualizarReserva(LoginRequiredMixin, UpdateView):
    template_name = 'reservas/atualizar.html'
    model = Reservas
    success_url = reverse_lazy('lista_laboratorios')
    form_class = AtualizarReservasForm
    pk_url_kwarg = 'res_codigo'

    def form_valid(self, form):
        reserva = form.save(commit=False)
        reserva.professor = self.request.user

        inicio_str = reserva.res_inicio.strftime('%Y-%m-%d %H:%M:%S')
        fim_str = reserva.res_fim.strftime('%Y-%m-%d %H:%M:%S')
        reserva.res_inicio = timezone.make_aware(
            datetime.strptime(inicio_str, '%Y-%m-%d %H:%M:%S'),
            timezone.get_current_timezone()
        )
        reserva.res_fim = timezone.make_aware(
            datetime.strptime(fim_str, '%Y-%m-%d %H:%M:%S'),
            timezone.get_current_timezone()
        )

        if not self._horario_disponivel(reserva):
            form.add_error(None, "O horário selecionado não está disponível ou conflita com outra reserva")
            return self.form_invalid(form)

        if reserva.res_repeticao != 'N':
            Reservas.objects.filter(res_repeticao_original=reserva).delete()

        reserva_base = form.save(commit=False)
        tipo_repeticao = reserva_base.res_repeticao

        if tipo_repeticao == "S":
            return self._salvar_repeticoes_semanais(form, reserva_base)
        elif tipo_repeticao == "D":
            return self._salvar_repeticoes_diarias(form, reserva_base)
        elif tipo_repeticao == "M":
            return self._salvar_repeticoes_mensais(form, reserva_base)
        elif tipo_repeticao == "A":
            return self._salvar_repeticoes_anuais(form, reserva_base)
        else:
            reserva_base.laboratorio.lab_status = 'usando'
            reserva_base.laboratorio.save()
            reserva_base.save()
            return super().form_valid(form)

    def _horario_disponivel(self, reserva):
        hora_inicio = reserva.res_inicio.astimezone(timezone.get_current_timezone()).replace(second=0, microsecond=0).time()
        hora_fim = reserva.res_fim.astimezone(timezone.get_current_timezone()).replace(second=0, microsecond=0).time()

        print(f"🚩 Verificando disponibilidade para horário ({hora_inicio} até {hora_fim})")

        disponibilidades = Disponibilidade.objects.filter(
            laboratorio=reserva.laboratorio,
            hor_inicio__lte=hora_inicio,
            hor_fim__gte=hora_fim
        )

        print(f"🚩 Disponibilidades encontradas: {disponibilidades}")

        if not disponibilidades.exists():
            print("❌ Nenhuma disponibilidade compatível encontrada.")
            return False

        conflitos = Reservas.objects.filter(
            laboratorio=reserva.laboratorio,
            res_inicio__lt=reserva.res_fim,
            res_fim__gt=reserva.res_inicio
        ).exclude(pk=reserva.pk if reserva.pk else None)

        if conflitos.exists():
            print("❌ Conflito detectado com outra reserva.")
            return False

        print("✅ Horário está livre e disponível.")
        return True

    def _salvar_repeticoes_semanais(self, form, reserva_base):
        inicio = reserva_base.res_inicio
        fim = reserva_base.res_fim
        dias_semana = form.cleaned_data["res_dia_semana"]
        intervalo = form.cleaned_data["res_intervalo_semanas"]
        data_limite = form.cleaned_data["res_data_final_repeticao"]

        reserva_base.laboratorio.lab_status = 'usando'
        reserva_base.laboratorio.save()
        reserva_base.save()

        dias_semana = [int(dia) for dia in dias_semana]
        data_atual = inicio.date()

        while data_atual <= data_limite:
            for dia in dias_semana:
                dia_reserva = self._proxima_data(data_atual, dia)
                if dia_reserva > data_limite:
                    continue
                dt_inicio = datetime.combine(dia_reserva, inicio.time())
                dt_fim = datetime.combine(dia_reserva, fim.time())

                nova_reserva = Reservas(
                    professor=self.request.user,
                    laboratorio=reserva_base.laboratorio,
                    res_inicio=dt_inicio,
                    res_fim=dt_fim,
                    res_repeticao='S',
                    res_descricao=reserva_base.res_descricao,
                    res_repeticao_original=reserva_base
                )
                if self._horario_disponivel(nova_reserva):
                    Reservas.objects.create(
                        professor=self.request.user,
                        laboratorio=reserva_base.laboratorio,
                        res_inicio=dt_inicio,
                        res_fim=dt_fim,
                        res_repeticao='S',
                        res_descricao=reserva_base.res_descricao,
                        res_repeticao_original=reserva_base
                    )
            data_atual += timedelta(weeks=intervalo)
        return super().form_valid(form)

    def _salvar_repeticoes_diarias(self, form, reserva_base):
        inicio = reserva_base.res_inicio
        fim = reserva_base.res_fim
        data_limite = form.cleaned_data["res_data_final_repeticao"]

        reserva_base.laboratorio.lab_status = 'usando'
        reserva_base.laboratorio.save()
        reserva_base.save()

        data_atual = inicio
        while data_atual.date() <= data_limite:
            dt_inicio = datetime.combine(data_atual.date(), inicio.time())
            dt_fim = datetime.combine(data_atual.date(), fim.time())

            nova_reserva = Reservas(
                professor=self.request.user,
                laboratorio=reserva_base.laboratorio,
                res_inicio=dt_inicio,
                res_fim=dt_fim,
                res_repeticao='D',
                res_descricao=reserva_base.res_descricao,
                res_repeticao_original=reserva_base
            )
            if self._horario_disponivel(nova_reserva):
                Reservas.objects.create(
                    professor=self.request.user,
                    laboratorio=reserva_base.laboratorio,
                    res_inicio=dt_inicio,
                    res_fim=dt_fim,
                    res_repeticao='D',
                    res_descricao=reserva_base.res_descricao,
                    res_repeticao_original=reserva_base
                )
            data_atual += timedelta(days=1)
        return super().form_valid(form)

    def _salvar_repeticoes_mensais(self, form, reserva_base):
        inicio = reserva_base.res_inicio
        fim = reserva_base.res_fim
        data_limite = form.cleaned_data["res_data_final_repeticao"]

        reserva_base.laboratorio.lab_status = 'usando'
        reserva_base.laboratorio.save()
        reserva_base.save()

        data_atual = inicio
        while data_atual.date() <= data_limite:
            dt_inicio = datetime.combine(data_atual.date(), inicio.time())
            dt_fim = datetime.combine(data_atual.date(), fim.time())

            nova_reserva = Reservas(
                professor=self.request.user,
                laboratorio=reserva_base.laboratorio,
                res_inicio=dt_inicio,
                res_fim=dt_fim,
                res_repeticao='M',
                res_descricao=reserva_base.res_descricao,
                res_repeticao_original=reserva_base
            )
            if self._horario_disponivel(nova_reserva):
                Reservas.objects.create(
                    professor=self.request.user,
                    laboratorio=reserva_base.laboratorio,
                    res_inicio=dt_inicio,
                    res_fim=dt_fim,
                    res_repeticao='M',
                    res_descricao=reserva_base.res_descricao,
                    res_repeticao_original=reserva_base
                )
            data_atual += relativedelta(months=1)
        return super().form_valid(form)

    def _salvar_repeticoes_anuais(self, form, reserva_base):
        inicio = reserva_base.res_inicio
        fim = reserva_base.res_fim
        data_limite = form.cleaned_data["res_data_final_repeticao"]

        reserva_base.laboratorio.lab_status = 'usando'
        reserva_base.laboratorio.save()
        reserva_base.save()

        data_atual = inicio
        while data_atual.date() <= data_limite:
            dt_inicio = datetime.combine(data_atual.date(), inicio.time())
            dt_fim = datetime.combine(data_atual.date(), fim.time())

            nova_reserva = Reservas(
                professor=self.request.user,
                laboratorio=reserva_base.laboratorio,
                res_inicio=dt_inicio,
                res_fim=dt_fim,
                res_repeticao='A',
                res_descricao=reserva_base.res_descricao,
                res_repeticao_original=reserva_base
            )
            if self._horario_disponivel(nova_reserva):
                Reservas.objects.create(
                    professor=self.request.user,
                    laboratorio=reserva_base.laboratorio,
                    res_inicio=dt_inicio,
                    res_fim=dt_fim,
                    res_repeticao='A',
                    res_descricao=reserva_base.res_descricao,
                    res_repeticao_original=reserva_base
                )
            data_atual += relativedelta(years=1)
        return super().form_valid(form)

    def _proxima_data(self, data_base, dia_semana):
        dias_ate_dia = (dia_semana - data_base.weekday() + 7) % 7
        return data_base + timedelta(days=dias_ate_dia)

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

