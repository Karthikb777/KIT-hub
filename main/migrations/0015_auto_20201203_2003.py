# Generated by Django 3.1.3 on 2020-12-03 14:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0014_auto_20201203_1916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notesofuser',
            name='note',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.note'),
        ),
        migrations.CreateModel(
            name='ModRequests',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]