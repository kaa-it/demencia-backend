# Generated by Django 3.2.9 on 2023-08-21 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demencia', '0006_auto_20220824_2218'),
    ]

    operations = [
        migrations.CreateModel(
            name='Instruction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Заполняется автоматически', verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Заполняется автоматически', verbose_name='Дата обновления')),
                ('name', models.CharField(help_text='Введите название', max_length=30, verbose_name='Название')),
                ('description', models.CharField(help_text='Введите описание', max_length=255, verbose_name='Описание')),
                ('file', models.FileField(help_text='Загрузите файл', upload_to='pdf/', verbose_name='Файл')),
                ('min_point', models.SmallIntegerField(help_text='Введите число', verbose_name='Минимальный балл')),
                ('max_point', models.SmallIntegerField(help_text='Введите число', verbose_name='Максимальный балл')),
                ('is_send', models.BooleanField(default=False, help_text='Включить/отключить отправку', verbose_name='Отправка пользователю')),
            ],
            options={
                'verbose_name': 'Инструкция',
                'verbose_name_plural': 'Инструкции',
                'ordering': ('name', '-is_send'),
            },
        ),
    ]
