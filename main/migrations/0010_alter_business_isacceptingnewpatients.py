# Generated by Django 3.2.7 on 2023-04-14 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20230413_1340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='isAcceptingNewPatients',
            field=models.CharField(choices=[('true', 'True'), ('false', 'False')], default='yes', max_length=255),
        ),
    ]