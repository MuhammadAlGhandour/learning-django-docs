# Generated by Django 4.2.2 on 2023-06-23 04:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='quesiton_text',
            new_name='question_text',
        ),
    ]
