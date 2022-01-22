# Generated by Django 3.2.9 on 2022-01-22 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demencia', '0006_auto_20220122_1656'),
    ]

    operations = [
        migrations.RenameField(
            model_name='settings',
            old_name='fund_section_link',
            new_name='fund_section_url_label',
        ),
        migrations.RenameField(
            model_name='settings',
            old_name='main_section_label',
            new_name='main_section_button_label',
        ),
        migrations.RenameField(
            model_name='settings',
            old_name='news_section_link',
            new_name='news_section_url_label',
        ),
        migrations.RemoveField(
            model_name='settings',
            name='about_section_link',
        ),
        migrations.RemoveField(
            model_name='settings',
            name='about_section_term_link',
        ),
        migrations.AddField(
            model_name='settings',
            name='about_section_button_label',
            field=models.CharField(default='Пройти тест', max_length=255, verbose_name='Название кнопки для прохождения теста'),
        ),
        migrations.AddField(
            model_name='settings',
            name='about_section_term_close_label',
            field=models.CharField(default='Скрыть', max_length=255, verbose_name='Название кнопки для скрытия термина'),
        ),
        migrations.AddField(
            model_name='settings',
            name='about_section_term_open_label',
            field=models.CharField(default='Подробнее', max_length=255, verbose_name='Название кнопки для раскрытия термина'),
        ),
        migrations.AlterField(
            model_name='settings',
            name='map_section_subtitle',
            field=models.CharField(default='Карта центров профилактики', max_length=255, verbose_name='Подзаголовок секции'),
        ),
        migrations.AlterField(
            model_name='settings',
            name='partners_section_subtitle',
            field=models.CharField(default='Партнеры', max_length=255, verbose_name='Подзаголовок секции'),
        ),
    ]
