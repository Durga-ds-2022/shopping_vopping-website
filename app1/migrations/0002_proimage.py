# Generated by Django 4.1.3 on 2022-11-24 11:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=None)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='productimage', to='app1.product')),
            ],
        ),
    ]
