from django.shortcuts import render

# Create your views here.
def inicio(request):
    return render(request, 'core/inicio.html')
    
def about(request):
    return render(request, 'core/about.html')

def login(request):
    return render(request, 'core/login.html')