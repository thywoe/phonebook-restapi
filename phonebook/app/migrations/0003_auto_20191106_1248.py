# Generated by Django 2.2.7 on 2019-11-06 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20191105_1923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phonebook',
            name='address',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='phonebook',
            name='email',
            field=models.EmailField(max_length=254, null=True, unique=True),
        ),
    ]