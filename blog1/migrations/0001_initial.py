# Generated by Django 3.2 on 2021-05-15 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contect',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('phone', models.CharField(max_length=13)),
                ('text', models.TextField(max_length=500)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]