# Generated by Django 3.2.7 on 2023-04-13 06:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20230413_1130'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='business',
            name='publisher_id',
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_id', models.URLField()),
                ('business', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.business')),
            ],
        ),
    ]
