# Generated by Django 5.0.1 on 2024-02-01 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_option_product_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField()),
                ('main_video', models.FileField(upload_to='')),
                ('whastapp', models.CharField(max_length=200)),
                ('wechat', models.CharField(max_length=200)),
            ],
        ),
    ]