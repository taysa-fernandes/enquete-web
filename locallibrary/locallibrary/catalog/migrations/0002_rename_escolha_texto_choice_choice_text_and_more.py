# Generated by Django 4.1.5 on 2023-01-22 15:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='escolha_texto',
            new_name='choice_text',
        ),
        migrations.RenameField(
            model_name='choice',
            old_name='votos',
            new_name='votes',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='data_pub',
            new_name='date_pub',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='texto_questao',
            new_name='question_text',
        ),
    ]
