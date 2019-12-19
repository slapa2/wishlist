# Generated by Django 3.0.1 on 2019-12-19 22:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gifts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gift',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=200)),
                ('img_url', models.CharField(max_length=400)),
                ('gift_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gifts.GiftsList')),
            ],
        ),
        migrations.CreateModel(
            name='GiftUrl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=400)),
                ('gift', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gifts.Gift')),
            ],
        ),
    ]