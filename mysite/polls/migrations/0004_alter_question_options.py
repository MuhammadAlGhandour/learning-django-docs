# Generated by Django 4.2.2 on 2023-06-30 13:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_alter_question_pub_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='question',
            options={'ordering': ['-pub_date']},
        ),
    ]