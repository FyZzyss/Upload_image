# Generated by Django 3.0.7 on 2020-06-23 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='hash',
            field=models.CharField(default=1, max_length=64),
            preserve_default=False,
        ),
    ]
