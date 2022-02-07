# Generated by Django 3.2.9 on 2022-02-02 12:14

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('demencia', '0012_alter_region_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsarticle',
            name='text',
            field=tinymce.models.HTMLField(help_text='Введите текст', verbose_name='Текст новости'),
        ),
        migrations.AlterField(
            model_name='settings',
            name='map_section_info',
            field=models.TextField(verbose_name='Предупреждение'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='title',
            field=tinymce.models.HTMLField(help_text='Введите заголовок', max_length=250, verbose_name='Заголовок'),
        ),
    ]