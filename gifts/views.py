from django.shortcuts import render

from .models import GiftsList, Gift
from .forms import GiftsListForm


def get_gifts_list(request):
	if request.method == 'POST':
		form = GiftsListForm(request.POST)
		if form.is_valid():
			form.save()
	else:
		form = GiftsListForm()
	
	queryset = GiftsList.objects.all
	context = {
		'form': form,
		'queryset': queryset 
	}
	return render(request, 'gifts/gifts_list.html', context)

def get_gift(request, id):
	queryset = Gift.objects.filter(gift_list=id)
	context = {
		'queryset': queryset
	}
	return render(request, 'gifts/gifts.html', context)