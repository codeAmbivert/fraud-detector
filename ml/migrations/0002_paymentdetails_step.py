# Generated by Django 4.2.4 on 2024-05-20 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ml', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='paymentdetails',
            name='step',
            field=models.IntegerField(default=None),
            preserve_default=False,
        ),
    ]
