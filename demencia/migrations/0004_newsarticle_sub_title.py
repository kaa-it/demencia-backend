# Generated by Django 3.2.9 on 2022-01-20 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demencia', '0003_alter_settings_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsarticle',
            name='sub_title',
            field=models.CharField(default='текст подзоголовка', help_text='Введите подзаголовок', max_length=250, verbose_name='Подзаголовок'),
            preserve_default=False,
        ),
    ]
