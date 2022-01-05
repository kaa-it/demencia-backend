# Generated by Django 3.2.9 on 2022-01-05 12:32

from django.db import migrations, models
import phonenumber_field.modelfields
import tinymce.models


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
                ('name', models.CharField(max_length=250, verbose_name='Название элемента')),
                ('url', models.URLField(max_length=250, verbose_name='Ссылка')),
            ],
            options={
                'verbose_name': 'Элемент левого меню',
                'verbose_name_plural': 'Элементы левого меню',
                'ordering': ['-updated_at'],
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
                ('name', models.CharField(max_length=250, verbose_name='Название элемента')),
                ('url', models.URLField(max_length=250, verbose_name='Ссылка')),
            ],
            options={
                'verbose_name': 'Элемент главного меню',
                'verbose_name_plural': 'Элементы главного меню',
                'ordering': ['-updated_at'],
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
                ('city', models.CharField(max_length=250, verbose_name='Город')),
                ('address', models.CharField(help_text='Улица, дом, офис', max_length=250, verbose_name='Адрес в городе')),
                ('phone_no', phonenumber_field.modelfields.PhoneNumberField(help_text='Номер телефона с указанием кода', max_length=128, region=None, verbose_name='Номер телефона')),
            ],
            options={
                'verbose_name': 'Точка на карте',
                'verbose_name_plural': 'Точки на карте',
                'ordering': ['-updated_at'],
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
                ('text', models.TextField(help_text='Введите текст', verbose_name='Текст новости')),
                ('url', models.URLField(help_text='Введите адрес ссылки', max_length=250, verbose_name='Ссылка')),
                ('url_label', models.CharField(default='ПОДРОБНЕЕ', help_text='Введите текст ссылки', max_length=50, verbose_name='Название ссылки')),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
                'ordering': ['-updated_at'],
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
                ('image', models.ImageField(upload_to='partners/', verbose_name='Файл изображения')),
                ('name', models.CharField(help_text='Введите название партнёра', max_length=250, verbose_name='Название партнёра')),
                ('url', models.URLField(help_text='Введите адрес ссылки', max_length=250, verbose_name='Ссылка')),
            ],
            options={
                'verbose_name': 'Партнёр',
                'verbose_name_plural': 'Партнёры',
                'ordering': ['-updated_at'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_name', models.CharField(default='Деменция.net', max_length=255, verbose_name='Название сайта')),
                ('copyright', models.CharField(default='Благотворительный фонд «Память поколений»', max_length=255, verbose_name='Авторское право')),
                ('meta_description', models.TextField(verbose_name='Meta описание')),
                ('main_section_link', models.CharField(default='Пройти тест', max_length=255, verbose_name='Название ссылки')),
                ('main_section_additional', models.TextField(verbose_name='Доп. информация')),
                ('main_section_additional_link', models.CharField(default='Подробнее', max_length=255, verbose_name='Название ссылки для доп. информации')),
                ('main_section_additional_url', models.URLField(default='https://душевная.москва/ru-RU/moscow_nko/all_news/card/12871.html', max_length=255, verbose_name='Ссылка на ресурс доп. информации')),
                ('about_section', models.CharField(default='О деменции', max_length=255, verbose_name='Название секции')),
                ('about_section_term', tinymce.models.HTMLField(verbose_name='Определение термина')),
                ('about_section_term_link', models.CharField(default='Подробнее', max_length=255, verbose_name='Название ссылки для раскрытия термина')),
                ('about_section_action_title', models.CharField(default='Помоги близким', max_length=255, verbose_name='Заголовок действия')),
                ('about_section_action_subtitle', models.CharField(default='Пройди тест с тем кому нужна помощь', max_length=255, verbose_name='Подзаголовок действия')),
                ('about_section_info', tinymce.models.HTMLField(verbose_name='Информация о статистике')),
                ('about_section_link', models.CharField(default='Пройти тест', max_length=255, verbose_name='Название ссылки для прохождения теста')),
                ('news_section', models.CharField(default='Что нового?', max_length=255, verbose_name='Название секции')),
                ('news_section_link', models.CharField(default='Перейти к ленте новостей', max_length=255, verbose_name='Название ссылки')),
                ('partners_section', models.CharField(default='Кто с нами?', max_length=255, verbose_name='Название секции')),
                ('partners_section_subtitle', models.CharField(default='Партнеры', max_length=255, verbose_name='Название ссылки')),
                ('map_section', models.CharField(default='Куда идти?', max_length=255, verbose_name='Название секции')),
                ('map_section_subtitle', models.CharField(default='Карта центров профилактики', max_length=255, verbose_name='Название ссылки')),
                ('map_section_info', tinymce.models.HTMLField(verbose_name='Предупреждение')),
                ('fund_section', models.CharField(default='О фонде', max_length=255, verbose_name='Название секции')),
                ('fund_section_info', tinymce.models.HTMLField(verbose_name='Описание')),
                ('fund_section_link', models.CharField(default='Перейти на сайт фонда', max_length=255, verbose_name='Название ссылки')),
                ('fund_section_url', models.URLField(default='https://pamyatpokoleniy.ru/', max_length=255, verbose_name='Ссылка на сайт фонда')),
            ],
            options={
                'verbose_name': 'Системные настройки',
                'verbose_name_plural': 'Системные настройки',
            },
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Заполняется автоматически', verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Заполняется автоматически', verbose_name='Дата обновления')),
                ('is_active', models.BooleanField(default=True, help_text='Включить/отключить показ на сайте', verbose_name='Активность')),
                ('title', models.CharField(help_text='Введите заголовок', max_length=250, verbose_name='Заголовок')),
                ('image', models.ImageField(upload_to='slider/', verbose_name='Файл изображения')),
                ('url', models.URLField(help_text='Введите адрес ссылки', max_length=250, verbose_name='Ссылка')),
                ('url_label', models.CharField(default='ПОДРОБНЕЕ', help_text='Введите текст ссылки', max_length=50, verbose_name='Название ссылки')),
            ],
            options={
                'verbose_name': 'Слайд',
                'verbose_name_plural': 'Слайды',
                'ordering': ['-updated_at'],
                'abstract': False,
            },
        ),
    ]
