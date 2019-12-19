from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _

from .models import GiftsList


class GiftsListForm(ModelForm):
	class Meta:
		model = GiftsList
		fields = ['name']
		labels = {
            'name': _(''),
        }    