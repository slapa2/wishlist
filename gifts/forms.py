from django import forms
from django.utils.translation import gettext_lazy as _

from crispy_forms.layout import Submit

from .models import GiftsList


class GiftsListForm(forms.ModelForm):

	class Meta:
		model = GiftsList
		fields = ['name', 'password']
		labels = {
			'name': ('Nazwa twojej listy:'),
			'password': ('Hasło'),
        }