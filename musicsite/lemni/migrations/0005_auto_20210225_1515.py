# Generated by Django 3.1.5 on 2021-02-25 12:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lemni', '0004_auto_20210225_1514'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='album',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.RESTRICT, to='lemni.album'),
        ),
    ]
