# Generated by Django 3.2 on 2021-05-30 06:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book_store', '0033_auto_20210530_1124'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='payment',
            new_name='mode',
        ),
    ]