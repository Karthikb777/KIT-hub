# Generated by Django 3.1.3 on 2020-11-29 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='coverImage',
            field=models.ImageField(default=1, upload_to='images/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='note',
            name='uniqueCode',
            field=models.IntegerField(default=7380368),
        ),
    ]
