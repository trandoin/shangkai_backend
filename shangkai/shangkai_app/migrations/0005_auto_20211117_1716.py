# Generated by Django 3.2.7 on 2021-11-17 11:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_auto_20211116_2007'),
        ('shangkai_app', '0004_comments_all'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments_all',
            name='user',
        ),
        migrations.AddField(
            model_name='comments_all',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='users.normal_userreg'),
        ),
    ]
