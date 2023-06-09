from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, RemoveUser
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


def home(request):
    return render(request, 'users/home.html')


def register_user(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Hi, {username}! Your account was created successfully.')
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required()
def profile(request):
    return render(request, 'users/profile.html')


def edit_email(request):
    if request.method == 'POST':
        email = request.POST['email']

        User.objects.filter(username=request.user).update(email=email)
    return render(request, 'users/profile.html')


def remove_user(request):

    if request.method == 'GET':
        form = RemoveUser(request.GET)
        rem = User.objects.get(username=request.user)
        if rem is not None:
            rem.delete()
        else:
            return render(request, 'users/profile.html')
    else:
        form = RemoveUser()
    return redirect('home')


def handler404(request, exception):
    return render(request, 'users/page_404.html')
