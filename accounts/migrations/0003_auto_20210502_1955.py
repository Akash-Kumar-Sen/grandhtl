# Generated by Django 3.1 on 2021-05-02 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20210427_1212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='phone_number',
            field=models.CharField(max_length=50),
        ),
    ]
