# Generated by Django 4.1.3 on 2022-12-14 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0008_order_productinorder_delete_paymentdetails'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='razorpay_signature',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
