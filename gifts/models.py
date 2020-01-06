from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class GiftsList(models.Model):
    name = models.CharField(max_length=200, default='')
    slug = models.SlugField(default='')
    password = models.CharField(max_length=200, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('gifts_list_detail_view', kwargs={"pk": str(self.pk)})
    

class Gift(models.Model):
    name = models.CharField(max_length=200)
    status = models.CharField(max_length=200)
    img_url = models.CharField(max_length=400)
    gift_list = models.ForeignKey(GiftsList, on_delete=models.CASCADE)

class GiftUrl(models.Model):
    url = models.CharField(max_length=400)
    gift = models.ForeignKey(Gift, on_delete=models.CASCADE)