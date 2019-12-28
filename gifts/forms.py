from django import forms
from django.utils.translation import gettext_lazy as _

from crispy_forms.layout import Submit

from .models import GiftsList


class GiftsListForm(forms.ModelForm):

	class Meta:
		model = GiftsList
		fields = ['owner', 'name', 'password']
		labels = {
            'owner': _('Jak się nazywasz?'),
			'name': ('Nazwa twojej listy:'),
			'password': ('Hasło'),
        }