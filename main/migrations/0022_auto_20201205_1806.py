# Generated by Django 3.1.3 on 2020-12-05 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_auto_20201204_2032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='file',
            field=models.FileField(upload_to='files/'),
        ),
    ]
