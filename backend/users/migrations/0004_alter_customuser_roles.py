# Generated by Django 4.2.1 on 2024-11-12 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_customuser_roles'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='roles',
            field=models.CharField(choices=[('user', 'User'), ('admin', 'Admin')], default='user', max_length=12),
        ),
    ]
