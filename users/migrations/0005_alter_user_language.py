# Generated by Django 3.2.9 on 2024-01-22 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20240122_1016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='language',
            field=models.CharField(blank=True, choices=[('uz', 'Uzbek'), ('ru', 'Russian')], max_length=2, null=True),
        ),
    ]
