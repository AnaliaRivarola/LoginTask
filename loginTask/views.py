# login_task/views.py
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

def custom_login(request):
    if request.method == 'POST':
        email = request.POST['email']  # Usamos 'email' en lugar de 'username' para coincidir con el nombre del campo en el formulario
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)  # Utilizamos 'email' como el campo de autenticación
        if user is not None:
            login(request, user)
            return redirect('dashboard')  # Reemplaza 'dashboard' con la URL a la que quieres redirigir después del inicio de sesión exitoso
        else:
            # Handle authentication failure
            pass
    return render(request, 'login_task/login.html')  # Ruta a la plantilla de inicio de sesión

@login_required
def dashboard(request):
    # Vista para la página de inicio después del inicio de sesión
    return render(request, 'dashboard.html')  # Reemplaza 'dashboard.html' con la plantilla de tu página de inicio
