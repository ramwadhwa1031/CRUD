# Generated by Django 2.2.2 on 2019-12-26 08:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('satsangi_register', '0002_auto_20191226_1353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='job',
            field=models.ForeignKey(default=' nothing', on_delete=django.db.models.deletion.CASCADE, to='satsangi_register.Job'),
        ),
    ]