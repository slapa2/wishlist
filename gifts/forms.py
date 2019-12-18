from django.forms import ModelForm
from .models import GiftsList

class GiftsListForm(ModelForm):
	class Meta:
		model = GiftsList
		fields = ['name']