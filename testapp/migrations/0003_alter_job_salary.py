# Generated by Django 4.2.4 on 2023-09-05 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0002_book_customer_job'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='salary',
            field=models.IntegerField(),
        ),
    ]