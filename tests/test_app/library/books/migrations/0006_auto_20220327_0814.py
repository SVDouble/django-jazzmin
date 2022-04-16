# Generated by Django 3.2.12 on 2022-03-27 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("books", "0005_book_last_print"),
    ]

    operations = [
        migrations.AlterField(
            model_name="author",
            name="id",
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID"),
        ),
        migrations.AlterField(
            model_name="book",
            name="id",
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID"),
        ),
        migrations.AlterField(
            model_name="genre",
            name="id",
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID"),
        ),
    ]
