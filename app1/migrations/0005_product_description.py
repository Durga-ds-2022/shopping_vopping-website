# Generated by Django 4.1.3 on 2022-12-07 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_product_is_top5_alter_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
