# Generated by Django 2.0.5 on 2018-05-24 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parsed_data', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogdata',
            name='title',
            field=models.CharField(max_length=500),
        ),
    ]