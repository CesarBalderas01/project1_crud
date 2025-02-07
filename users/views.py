from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import User
from .forms import UserForm

def users_list(request):
    users = User.objects.all()
    form = UserForm()
    return render(request, 'users_list.html', {'users': users, 'form': form})

def create_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuario creado exitosamente.')
            return redirect('users_list')
        else:
            messages.error(request, 'Hubo un error en la creación del usuario.')
    else:
        form = UserForm()

    return redirect('users_list')

def edit_user(request, id):
    user = get_object_or_404(User, id=id)

    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuario actualizado correctamente.')
            return redirect('users_list')
        else:
            messages.error(request, 'Error al actualizar el usuario.')

    form = UserForm(instance=user)
    return render(request, 'users_list.html', {'users': User.objects.all(), 'form': form, 'edit_user': user})

def delete_user(request, id):
    user = get_object_or_404(User, id=id)
    user.delete()
    messages.success(request, 'Usuario Eliminado correctamente...')
    return redirect('users_list')
