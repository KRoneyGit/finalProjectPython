# Generated by Django 4.2 on 2023-04-27 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_recipe_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='category',
            field=models.CharField(max_length=50),
        ),
    ]
