from django.shortcuts import render

from .models import GiftsList, Gift
from .forms import GiftsListForm

def index(request):

	if request.method == 'POST':
		form = GiftsListForm(request.POST)
		if form.is_valid():
			form.save()
	else:
		form = GiftsListForm()
	
	template = 'gifts/gifts_list_create.html'
	context = {
		'form': form,
	}
	return render(request, template, context)