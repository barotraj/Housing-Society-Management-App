# Generated by Django 3.0.5 on 2020-04-22 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_event'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='city',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='description',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='website',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='address',
            field=models.CharField(default='Ground Floor', max_length=100),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='age',
            field=models.IntegerField(default=35),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='designation',
            field=models.CharField(default='Tenant', max_length=100),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='rent_paid',
            field=models.BooleanField(default=False),
        ),
    ]
