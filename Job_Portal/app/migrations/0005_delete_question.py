# Generated by Django 4.1.7 on 2023-03-26 15:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_question'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Question',
        ),
    ]