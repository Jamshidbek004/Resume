# Generated by Django 4.2.3 on 2024-11-12 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asosiy', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personalinfo',
            name='birth_year',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
