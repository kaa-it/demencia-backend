# Generated by Django 3.2.9 on 2022-04-04 17:40

import demencia.models
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields
import tinymce.models
import url_or_relative_url_field.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LeftMenuElement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Заполняется автоматически', verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Заполняется автоматически', verbose_name='Дата обновления')),
                ('is_active', models.BooleanField(default=True, help_text='Включить/отключить показ на сайте', verbose_name='Активность')),
                ('position', models.PositiveIntegerField(default=0, help_text='Можно поменять перетаскиванием на странице списка объектов', verbose_name='Позиция в списке')),
                ('name', models.CharField(max_length=250, unique=True, verbose_name='Название элемента')),
                ('url', url_or_relative_url_field.fields.URLOrRelativeURLField(max_length=250, verbose_name='Ссылка')),
            ],
            options={
                'verbose_name': 'Элемент левого меню',
                'verbose_name_plural': 'Элементы левого меню',
                'ordering': ['position'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MainMenuElement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Заполняется автоматически', verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Заполняется автоматически', verbose_name='Дата обновления')),
                ('is_active', models.BooleanField(default=True, help_text='Включить/отключить показ на сайте', verbose_name='Активность')),
                ('position', models.PositiveIntegerField(default=0, help_text='Можно поменять перетаскиванием на странице списка объектов', verbose_name='Позиция в списке')),
                ('name', models.CharField(max_length=250, unique=True, verbose_name='Название элемента')),
                ('url', url_or_relative_url_field.fields.URLOrRelativeURLField(max_length=250, verbose_name='Ссылка')),
            ],
            options={
                'verbose_name': 'Элемент главного меню',
                'verbose_name_plural': 'Элементы главного меню',
                'ordering': ['position'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='NewsArticle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Заполняется автоматически', verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Заполняется автоматически', verbose_name='Дата обновления')),
                ('is_active', models.BooleanField(default=True, help_text='Включить/отключить показ на сайте', verbose_name='Активность')),
                ('image', models.ImageField(upload_to='news/', verbose_name='Файл изображения')),
                ('title', models.CharField(help_text='Введите заголовок', max_length=250, verbose_name='Заголовок')),
                ('sub_title', models.CharField(help_text='Введите подзаголовок', max_length=250, verbose_name='Подзаголовок')),
                ('text', tinymce.models.HTMLField(help_text='Введите текст', verbose_name='Текст новости')),
                ('url', url_or_relative_url_field.fields.URLOrRelativeURLField(help_text='Введите адрес ссылки', max_length=250, verbose_name='Ссылка')),
                ('url_label', models.CharField(default='ПОДРОБНЕЕ', help_text='Введите текст ссылки', max_length=50, verbose_name='Название ссылки')),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
                'ordering': ['-created_at'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Заполняется автоматически', verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Заполняется автоматически', verbose_name='Дата обновления')),
                ('is_active', models.BooleanField(default=True, help_text='Включить/отключить показ на сайте', verbose_name='Активность')),
                ('position', models.PositiveIntegerField(default=0, help_text='Можно поменять перетаскиванием на странице списка объектов', verbose_name='Позиция в списке')),
                ('image', models.ImageField(upload_to='partners/', verbose_name='Файл изображения')),
                ('name', models.CharField(help_text='Введите название партнёра', max_length=250, verbose_name='Название партнёра')),
                ('url', models.URLField(help_text='Введите адрес ссылки', max_length=250, verbose_name='Ссылка')),
            ],
            options={
                'verbose_name': 'Партнёр',
                'verbose_name_plural': 'Партнёры',
                'ordering': ['position'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название субъекта')),
                ('geocode', models.CharField(max_length=20, verbose_name='Геокод')),
            ],
            options={
                'verbose_name': 'Регион',
                'verbose_name_plural': 'Регионы',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_name', models.CharField(default='Деменция.net', max_length=255, verbose_name='Название сайта')),
                ('copyright', models.CharField(default='Благотворительный фонд «Память поколений»', max_length=255, verbose_name='Авторское право')),
                ('meta_description', models.TextField(verbose_name='Meta описание')),
                ('main_section_button_label', models.CharField(default='Пройти тест', max_length=255, verbose_name='Название кнопки')),
                ('about_section', models.CharField(default='О деменции', max_length=255, verbose_name='Название секции')),
                ('about_section_term', tinymce.models.HTMLField(verbose_name='Определение термина')),
                ('about_section_term_open_label', models.CharField(default='Подробнее', max_length=255, verbose_name='Название кнопки для раскрытия термина')),
                ('about_section_term_close_label', models.CharField(default='Скрыть', max_length=255, verbose_name='Название кнопки для скрытия термина')),
                ('about_section_action_title', models.CharField(default='Помоги близким', max_length=255, verbose_name='Заголовок действия')),
                ('about_section_action_subtitle', models.CharField(default='Пройди тест с тем кому нужна помощь', max_length=255, verbose_name='Подзаголовок действия')),
                ('about_section_info', tinymce.models.HTMLField(verbose_name='Информация о статистике')),
                ('about_section_button_label', models.CharField(default='Пройти тест', max_length=255, verbose_name='Название кнопки для прохождения теста')),
                ('news_section', models.CharField(default='Что нового?', max_length=255, verbose_name='Название секции')),
                ('news_section_url_label', models.CharField(default='Перейти к ленте новостей', max_length=255, verbose_name='Название ссылки')),
                ('partners_section', models.CharField(default='Кто с нами?', max_length=255, verbose_name='Название секции')),
                ('partners_section_subtitle', models.CharField(default='Партнеры', max_length=255, verbose_name='Подзаголовок секции')),
                ('map_section', models.CharField(default='Куда идти?', max_length=255, verbose_name='Название секции')),
                ('map_section_subtitle', models.CharField(default='Карта центров профилактики', max_length=255, verbose_name='Подзаголовок секции')),
                ('map_section_info', models.TextField(verbose_name='Предупреждение')),
                ('fund_section', models.CharField(default='О фонде', max_length=255, verbose_name='Название секции')),
                ('fund_section_info', tinymce.models.HTMLField(verbose_name='Описание')),
                ('fund_section_url_label', models.CharField(default='Перейти на сайт фонда', max_length=255, verbose_name='Название ссылки')),
                ('fund_section_url', models.URLField(default='https://pamyatpokoleniy.ru/', max_length=255, verbose_name='Ссылка на сайт фонда')),
            ],
            options={
                'verbose_name': 'Настройки главной страницы',
                'verbose_name_plural': 'Настройки главной страницы',
            },
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Заполняется автоматически', verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Заполняется автоматически', verbose_name='Дата обновления')),
                ('is_active', models.BooleanField(default=True, help_text='Включить/отключить показ на сайте', verbose_name='Активность')),
                ('position', models.PositiveIntegerField(default=0, help_text='Можно поменять перетаскиванием на странице списка объектов', verbose_name='Позиция в списке')),
                ('title', demencia.models.SmallHTMLField(help_text='Введите заголовок', max_length=250, verbose_name='Заголовок')),
                ('image', models.ImageField(upload_to='slider/', verbose_name='Файл изображения')),
                ('url', url_or_relative_url_field.fields.URLOrRelativeURLField(help_text='Введите адрес ссылки', max_length=250, verbose_name='Ссылка')),
                ('url_label', models.CharField(default='ПОДРОБНЕЕ', help_text='Введите текст ссылки', max_length=50, verbose_name='Название ссылки')),
            ],
            options={
                'verbose_name': 'Слайд',
                'verbose_name_plural': 'Слайды',
                'ordering': ['position'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MapPoint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Заполняется автоматически', verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Заполняется автоматически', verbose_name='Дата обновления')),
                ('is_active', models.BooleanField(default=True, help_text='Включить/отключить показ на сайте', verbose_name='Активность')),
                ('position', models.PositiveIntegerField(default=0, help_text='Можно поменять перетаскиванием на странице списка объектов', verbose_name='Позиция в списке')),
                ('city', models.CharField(max_length=35, verbose_name='Город')),
                ('address', models.CharField(help_text='Улица, дом, офис', max_length=80, verbose_name='Адрес в городе')),
                ('phone_no', phonenumber_field.modelfields.PhoneNumberField(help_text='Номер телефона с указанием кода региона (пример: +7 495 933 00 20 или 8 495 933 00 20)', max_length=20, region='RU', verbose_name='Номер телефона')),
                ('phone_no_secondary', phonenumber_field.modelfields.PhoneNumberField(blank=True, help_text='Номер телефона с указанием кода региона (пример: +7 495 933 00 20 или 8 495 933 00 20)', max_length=20, region='RU', verbose_name='Номер телефона (доп.)')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='centers', to='demencia.region', verbose_name='Регион')),
            ],
            options={
                'verbose_name': 'Точка на карте',
                'verbose_name_plural': 'Точки на карте',
                'ordering': ['position'],
                'abstract': False,
            },
        ),
    ]
