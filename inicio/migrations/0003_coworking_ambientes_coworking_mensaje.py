# Generated by Django 5.1.1 on 2024-10-25 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0002_coworking_delete_auto'),
    ]

    operations = [
        migrations.AddField(
            model_name='coworking',
            name='ambientes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='coworking',
            name='mensaje',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
    ]