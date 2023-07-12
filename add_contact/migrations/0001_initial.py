# Generated by Django 4.0 on 2023-06-26 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AddContact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone1', models.CharField(blank=True, max_length=50)),
                ('email', models.EmailField(max_length=100)),
                ('picture', models.ImageField(blank=True, upload_to='pic')),
                ('address', models.CharField(blank=True, max_length=150)),
                ('business_key', models.CharField(max_length=50)),
                ('textfield', models.TextField(max_length=300)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]