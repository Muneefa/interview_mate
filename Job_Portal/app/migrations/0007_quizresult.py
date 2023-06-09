# Generated by Django 4.1.7 on 2023-04-02 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_question'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuizResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('score', models.IntegerField()),
                ('field', models.CharField(max_length=200)),
            ],
        ),
    ]
