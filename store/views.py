from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm, LoginForm

def main(request):
    return render(request, 'store/index.html')

@login_required
def profile(request):
    return render(request, 'store/profile.html')

def user_register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('profile')  # Перенаправление на `/profile/`
    else:
        form = RegistrationForm()
    return render(request, 'store/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('profile')  # Перенаправление на `/profile/`
        else:
            return render(request, 'store/login.html', {'form': form, 'error': 'Неправильный логин или пароль'})
    else:
        form = LoginForm()

    return render(request, 'store/login.html', {'form': form})

@login_required
def user_logout(request):
    logout(request)
    return redirect('login')
