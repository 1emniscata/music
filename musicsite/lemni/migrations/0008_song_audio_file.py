# Generated by Django 3.1.5 on 2021-02-26 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lemni', '0007_auto_20210225_1754'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='audio_file',
            field=models.FileField(default='', upload_to=''),
        ),
    ]