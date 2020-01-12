from slugify import slugify

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

    @staticmethod
    def create_default_gifts_list(user):
        default_gifts_list_name = 'moja lista prezentów'
        gifts_list = GiftsList(
            name=default_gifts_list_name,
            slug=slugify(' '.join((user.username, default_gifts_list_name))),
            password=None,
            owner=user
        )
        gifts_list.save()
    

class Gift(models.Model):
    name = models.CharField(max_length=200)
    status = models.CharField(max_length=200, blank=True, null=True)
    img_url = models.CharField(max_length=400, blank=True, null=True)
    gifts_list = models.ForeignKey(GiftsList, on_delete=models.CASCADE)

class GiftUrl(models.Model):
    url = models.CharField(max_length=400)
    gift = models.ForeignKey(Gift, on_delete=models.CASCADE)