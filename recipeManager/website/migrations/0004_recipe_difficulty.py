# Generated by Django 4.2 on 2023-04-27 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_alter_recipe_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='difficulty',
            field=models.CharField(default='Easy', max_length=10),
        ),
    ]
