# Generated by Django 3.0.1 on 2020-01-11 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gifts', '0005_auto_20200106_1242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gift',
            name='img_url',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='gift',
            name='status',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
