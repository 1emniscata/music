# Generated by Django 3.1.5 on 2021-02-25 12:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lemni', '0003_auto_20210224_1957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='album',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.RESTRICT, to='lemni.album'),
        ),
    ]
