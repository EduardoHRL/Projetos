from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),

    # Urls do login, cadastro e logout
    path('login/', views.logar, name='login'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('logout/', views.sair, name='logout'),

    # Urls dos laboratórios
    path('laboratorios/admin', views.AdminLaboratoriosListView.as_view(), name='admin_lista_laboratorios'),
    path('laboratorios/', views.LaboratoriosListView.as_view(), name='lista_laboratorios'),
    path('laboratorios/cadastrar', views.LaboratoriosCreateView.as_view(), name='cadastra_laboratorios'),
    path('laboratorios/excluir/<str:lab_codigo>/', views.LaboratoriosDeleteView.as_view(), name='exclui_laboratorios'),
    path('laboratorios/atualizar/<str:lab_codigo>/', views.LaboratoriosUpdateView.as_view(), name='atualiza_laboratorios'),

    # Urls dos usuários
    path('usuarios/', views.UsuariosListView.as_view(), name='lista_usuarios'),
    path('usuarios/atualizar/<int:pk>/', views.atualiza_usuarios, name='atualiza_usuarios'),
    path('usuarios/excluir/<int:pk>/', views.excluir_usuario, name='excluir_usuario'),

    path('usuarios/rejeitar/<int:user_id>/', views.rejeitar_usuario, name='rejeitar_usuario'),
    path('usuarios/aprovar/<int:user_id>/', views.aprovar_usuario, name='aprovar_usuario'),

    # Urls da agenda
    path('agenda/', views.agenda, name='agenda'),
    path('eventos/json/', views.reservas_json, name='reservas_json'),
    path('agenda/criar', views.CriarReserva.as_view(), name='criar_reserva'),

    # Urls das reservas
    path('reservas/reservar/<int:lab_codigo>/', views.CriarReserva.as_view(), name='reservar'),
    path('reservas/atualizar/<int:pk>/', views.AtualizarReserva.as_view(), name='atualizar_reserva'),
    path('reservas/excluir/<int:pk>/', views.ExcluirReserva.as_view(), name='excluir_reserva'),
    path('historico/', views.historico_reservas, name='historico'),
    path('historico/admin', views.historico_reservas_admin, name='historico_admin'),

    # Urls da escola
    path('escola/informações/', views.EscolaUpdateView.as_view(), name='escola'),
    path('buscar-cep/', views.buscar_cep, name='buscar-cep'),
    path('escola/', views.EscolaListView.as_view(), name='informacoes_escola'),

    # Urls de recuperação de senha
    path('senha-reset/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form.html',
            email_template_name='registration/password_reset_email.txt',
            subject_template_name='registration/password_reset_subject.txt'), name='password_reset'),
            
    path('senha-reset/enviado/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('senha-reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('senha-reset/feito/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    path('api/laboratorios/<int:lab_codigo>/horarios/', views.horarios_laboratorio, name='horarios_laboratorio'),
    path('verificar-disponibilidade/<int:lab_codigo>/', views.verificar_disponibilidade, name='verificar_disponibilidade'),
    path('api/laboratorios/<int:lab_codigo>/horarios-disponiveis/', views.horarios_disponiveis, name='horarios_disponiveis'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)