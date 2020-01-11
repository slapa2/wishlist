from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

from gifts.models import GiftsList

def register_user_view(request):

    # redirect already authenticated user
    if request.user.is_authenticated:
        return redirect(settings.LOGIN_REDIRECT_URL)

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            GiftsList.create_default_gifts_list(user)
            return redirect('login')
    else:
        form = UserCreationForm()

    template = 'registration/register.html'
    context = {'form': form}
    return render(request, template, context)

@login_required
def home_page_view(request):
    user_lists = GiftsList.objects.filter(owner=request.user)

    template = 'users/home_page.html'
    context= {'user_lists': user_lists}
    return render(request, template, context)
