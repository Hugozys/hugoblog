# Generated by Django 2.1.5 on 2019-01-19 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0005_auto_20190119_0237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(verbose_name='date published'),
        ),
    ]
