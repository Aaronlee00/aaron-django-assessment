# Generated by Django 4.1.3 on 2022-11-16 16:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("aaronapp", "0004_rename_aa_data"),
    ]

    operations = [
        migrations.RenameField(
            model_name="data",
            old_name="input",
            new_name="keyin",
        ),
    ]
