# Generated by Django 4.0.6 on 2022-08-31 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_remove_todo_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='date',
            field=models.DateField(default=0.16666666666666666),
            preserve_default=False,
        ),
    ]
