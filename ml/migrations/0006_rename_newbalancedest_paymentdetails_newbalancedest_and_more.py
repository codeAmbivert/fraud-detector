# Generated by Django 5.0.6 on 2024-05-22 10:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ml', '0005_rename_oldbalanceorig_paymentdetails_oldbalanceorg'),
    ]

    operations = [
        migrations.RenameField(
            model_name='paymentdetails',
            old_name='newBalanceDest',
            new_name='newbalanceDest',
        ),
        migrations.RenameField(
            model_name='paymentdetails',
            old_name='newBalanceOrig',
            new_name='newbalanceOrig',
        ),
        migrations.RenameField(
            model_name='paymentdetails',
            old_name='oldBalanceDest',
            new_name='oldbalanceDest',
        ),
        migrations.RenameField(
            model_name='paymentdetails',
            old_name='oldBalanceOrg',
            new_name='oldbalanceOrg',
        ),
    ]
