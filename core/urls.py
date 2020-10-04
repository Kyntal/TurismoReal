from django.urls import path
from django.contrib.auth.decorators import login_required
from  .views import inicio, about
from core.usuario.views import Login,logoutUsuario,registerPage

urlpatterns = [
    path('inicio/', inicio, name="inicio"),
    path('about/', about, name="about"),
    path('accounts/login/', Login.as_view(template_name='core/login.html'), name='login'),
    path('', login_required(logoutUsuario), name='logout'),
    path('registro/', registerPage, name='registro_usuario'),
]
