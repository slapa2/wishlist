from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import GiftsList, Gift
from .forms import GiftsListForm, GiftForm

# GIFTS_LIST:
@login_required
def gifts_list_create_view(request):
	if request.method == 'POST':
		form = GiftsListForm(request.POST)
		if form.is_valid():
			obj = form.save(commit=False)
			obj.owner = request.user
			obj = form.save()
			return redirect(gifts_list_detail_view, pk=obj.pk)
	else:
		form = GiftsListForm()
	
	template = 'gifts/gift_form.html'
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


# GIFTS:
#---------------------------------------------------------------------------------------------
@login_required
def gift_create_view(request, gifts_list_pk):

	gifts_list = get_object_or_404(GiftsList, pk=gifts_list_pk)
	if request.method == 'POST':
		form = GiftForm(request.POST)
		if form.is_valid():
			obj = form.save(commit=False)
			obj.gifts_list = gifts_list
			obj.save()
			return redirect(gifts_list_detail_view, pk=gifts_list.pk)
	else:
		form = GiftForm()

	template = 'gifts/gift_form.html'
	context = {
		'form': form,
		'gifts_list': gifts_list,
	}
	return render(request, template, context)

def gift_detail_view(request, gift_pk):
	obj = get_object_or_404(Gift, pk=gift_pk)

	template = 'gifts/gift_detail.html'
	context = {'object': obj}
	return render(request, template, context)

@login_required
def gift_update_view(request, gift_pk):
	obj = get_object_or_404(Gift, pk=gift_pk)
	form = GiftForm(request.POST or None, instance=obj)
	if form.is_valid():
		form.save()
		return redirect(gift_detail_view, gift_pk=obj.pk)

	template = 'gifts/gift_form.html',
	context = { 'form': form, 'object': obj}
	return render(request, template, context)

@login_required
def gift_delete_view(request, gift_pk):
	obj = get_object_or_404(Gift, pk=gift_pk)
	gifts_list = obj.gifts_list
	if request.method == 'POST':
		obj.delete()
		return redirect(gifts_list_detail_view, pk=gifts_list.pk)

	template = 'gifts/gift_delete_confirm.html'
	context = {
		'object': obj,
		'gifts_list': gifts_list,
	}
	return render(request, template, context)