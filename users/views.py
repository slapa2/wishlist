from slugify import slugify

from django.shortcuts import render, redirect

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

from gifts.models import GiftsList

def register_user_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()

            # create default user gifts_list
            gifts_list_name = 'moja lista prezentów' 
            default_gifts_list = GiftsList(
                name = gifts_list_name,
                slug = slugify(' '.join((user.username, gifts_list_name))),
                password = None,
                owner = user
            )
            default_gifts_list.save()

            # login created user
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)

            return redirect('gifts_list_detail_view', pk=default_gifts_list.pk)
    else:
        form = UserCreationForm()

    template = 'registration/register.html'
    context = {'form': form}
    return render(request, template, context)


