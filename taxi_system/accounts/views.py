from django.shortcuts import render, redirect
from .forms import DriverRegistrationForm
from django.contrib.auth.models import User
from django.contrib.auth import  login, logout
from .models import Driver

# Create your views here.
def home(request):
    return render(request, 'accounts/home.html')
 
# def driver_register(request):
#     form = DriverRegistrationForm()
#     message = ""

#     if request.method == "POST":
#         form = DriverRegistrationForm(request.POST)

#         if form.is_valid():
#             # Create User
#             user = User.objects.create_user(
#                 username=form.cleaned_data['username'],
#                 password=form.cleaned_data['password']
#             )

#             # Create Driver profile
#             Driver.objects.create(
#                 usario=user,

#                 Telefono=form.cleaned_data['telefono'],
#                 No_Licencia=form.cleaned_data['no_licencia'],
#                 Matricula=form.cleaned_data['matricula']
#             )

#             # Auto login
#             login(request, user)
#             return redirect('dashbord')

#         else:
#             message = "Porfavor sanearlos errores en el formulario."

#     return render(request, 'accounts/driver_register.html', {
#         'form': form,
#         'message': message
#    })
def driver_register(request):
    if request.method == "POST":
        form = DriverRegistrationForm(request.POST)

        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )

            Driver.objects.create(
                usario=user,
                Telefono=form.cleaned_data['telefono'],
                No_Licencia=form.cleaned_data['no_licencia'],
                Matricula=form.cleaned_data['matricula']
            )

            login(request, user)
            return redirect('dashbord')
        else:
            print(form.errors)

    else:
        form = DriverRegistrationForm()

    return render(request, 'accounts/driver_register.html', {'form': form})