# Generated by Django 3.1.3 on 2020-11-23 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_system_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='allow_fields',
            field=models.IntegerField(choices=[(0, 'Email'), (1, 'Username'), (2, 'FirstName'), (3, 'LastName'), (4, 'Phone'), (5, 'Skype')], default=0),
        ),
    ]
