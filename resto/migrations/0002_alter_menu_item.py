# Generated by Django 4.0.4 on 2022-05-19 04:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resto', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='OrderItem', to='resto.orderitem'),
        ),
    ]