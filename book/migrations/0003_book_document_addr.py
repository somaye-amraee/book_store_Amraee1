# Generated by Django 3.2.4 on 2021-09-01 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_remove_book_document_addr'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='document_addr',
            field=models.FileField(blank=True, null=True, upload_to='documents/'),
        ),
    ]
