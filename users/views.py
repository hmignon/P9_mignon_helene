from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import DeleteView

from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from .models import UserFollow


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been created! You are now able to log in.')
            return redirect('login')

    else:
        form = UserRegisterForm()

    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)


@login_required
def subscriptions(request):
    user_follows = UserFollow.objects.filter(user=request.user)
    followed_by = UserFollow.objects.filter(followed_user=request.user)

    context = {
        'user_follows': user_follows,
        'followed_by': followed_by,
        'title': 'Subscriptions',
    }

    return render(request, 'users/subscriptions.html', context)


class UnsubscribeView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = UserFollow
    success_url = 'subscriptions/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user:
            return True
        return False
