# Generated by Django 5.0.1 on 2024-01-26 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_product'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CarBrand',
            new_name='Brand',
        ),
        migrations.RenameModel(
            old_name='CarModel',
            new_name='Model',
        ),
        migrations.RenameModel(
            old_name='CarSubmodel',
            new_name='Submodel',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='models',
            new_name='submodel',
        ),
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='product',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='prev_price',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
