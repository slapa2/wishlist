from django.shortcuts import render, redirect, get_object_or_404

from .models import GiftsList, Gift
from .forms import GiftsListForm

def index(request):

	if request.method == 'POST':
		form = GiftsListForm(request.POST)
		if form.is_valid():
			# obj= form.save(commit=False)
			obj = form.save()
			return redirect(gifts_list_detail_view, pk=obj.pk)
	else:
		form = GiftsListForm()
	
	template = 'gifts/gifts_list_create.html'
	context = {
		'form': form,
	}
	return render(request, template, context)

def gifts_list_detail_view(request, pk):
	obj = obj = get_object_or_404(GiftsList, pk=pk)
	template = 'gifts/gifts_list_detail_view.html'
	context = {
		'object': obj
	}
	return render(request, template, context)