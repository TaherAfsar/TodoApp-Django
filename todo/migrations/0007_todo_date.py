# Generated by Django 4.0.6 on 2022-08-31 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0006_remove_todo_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='date',
            field=models.CharField(default=0.16666666666666666, max_length=100),
            preserve_default=False,
        ),
    ]
