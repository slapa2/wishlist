from slugify import slugify

from django.shortcuts import render, redirect


from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

from gifts.models import GiftsList

def register_user_view(request):

    # redirect already authenticated user
    if request.user.is_authenticated:
        return redirect('user_home_page_view')

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()

            # create default user gifts_list after user register
            gifts_list_name = 'moja lista prezentów' 
            default_gifts_list = GiftsList(
                name = gifts_list_name,
                slug = slugify(' '.join((user.username, gifts_list_name))),
                password = None,
                owner = user
            )
            default_gifts_list.save()
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
