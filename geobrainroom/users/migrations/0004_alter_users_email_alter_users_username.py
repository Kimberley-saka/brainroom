# Generated by Django 4.2.6 on 2023-10-22 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_users_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='email',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='users',
            name='username',
            field=models.CharField(max_length=250),
        ),
    ]
