# Generated by Django 2.2 on 2020-01-08 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0003_auto_20200107_1712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feed',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
