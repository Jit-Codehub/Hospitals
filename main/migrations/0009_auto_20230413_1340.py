# Generated by Django 3.2.7 on 2023-04-13 08:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20230413_1326'),
    ]

    operations = [
        migrations.RenameField(
            model_name='areaserved',
            old_name='area_id',
            new_name='url',
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='emp_id',
            new_name='url',
        ),
        migrations.RenameField(
            model_name='haspart',
            old_name='h_type',
            new_name='type',
        ),
        migrations.RenameField(
            model_name='haspart',
            old_name='haspart_id',
            new_name='url',
        ),
    ]