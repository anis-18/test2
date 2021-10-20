# Generated by Django 3.2.8 on 2021-10-20 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='latitude',
            field=models.DecimalField(blank=True, decimal_places=16, max_digits=22, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='longitude',
            field=models.DecimalField(blank=True, decimal_places=16, max_digits=22, null=True),
        ),
    ]
