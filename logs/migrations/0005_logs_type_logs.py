# Generated by Django 3.2.9 on 2021-12-15 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logs', '0004_alter_logs_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='logs',
            name='type_logs',
            field=models.CharField(default='m', max_length=5),
        ),
    ]
