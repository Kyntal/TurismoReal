from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.generic.edit import FormView
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import formLog, FormularioLogin
from .models import User
from django.contrib.auth.models import User as Usuario
# Create your views here.
def crearUser(user, contrasena):
    #Guarda la instancia creada en usuario
    usuario = Usuario.objects.create_user(username = user, password = contrasena)
    #Se modifica si está activo o no
    usuario.is_active = True
    #Se guarda al usuario
    usuario.save()


def iniciar_sesion(request):
    #Se van a recibir los datos que se están enviando en el POST
    if request.method == 'POST':
        form = formLog(request.POST)
        #Si lo que recibe fue un post, y el formulario el válido
        if form.is_valid():
            # guarda lo que tiene el formulario
            form.save()
            #Toma los datos individualmente del formulario
            user = request.POST['usuario']
            contrasena = request.POST['contrasena']
            #Llama a la funcion para crear un usuario, se le envía el nombre de usuaio y el email
            crearUser(user, contrasena)
        return redirect('inicio')
    #En el caso de que fuera un GET, despliega el formulario
    else:
        form = formLog()
    return render(request, 'registration/registro.html', {'form': form})


class Login(FormView):
    template_name = 'login.html'
    form_class = FormularioLogin
    success_url = reverse_lazy('inicio')

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self,request,*args,**kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(Login,self).dispatch(request,*args,**kwargs)

    def form_valid(self,form):
        login(self.request,form.get_user())
        return super(Login,self).form_valid(form)

def logoutUsuario(request):
    logout(request)
    return HttpResponseRedirect('accounts/login/')

def registerPage(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form':form}
    return render(request, 'registration/registro.html', context)