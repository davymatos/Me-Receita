# Generated by Django 3.0.8 on 2020-07-30 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='receita',
            name='principal',
        ),
        migrations.AlterField(
            model_name='receita',
            name='ingredientes',
            field=models.TextField(blank=True, null=True),
        ),
    ]
