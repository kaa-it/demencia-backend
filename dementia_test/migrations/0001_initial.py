# Generated by Django 3.2.9 on 2022-02-02 20:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DementiaTestCase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Заполняется автоматически', verbose_name='Дата создания')),
            ],
            options={
                'verbose_name': 'Прохождение теста',
                'verbose_name_plural': 'Прохождения тестов',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Заполняется автоматически', verbose_name='Дата создания')),
                ('answer_value', models.CharField(max_length=255, verbose_name='Значение ответа')),
                ('question', models.PositiveSmallIntegerField(verbose_name='Номер вопроса')),
                ('test_case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dementia_test.dementiatestcase', verbose_name='Прохождение теста')),
            ],
            options={
                'verbose_name': 'Ответ на вопрос',
                'verbose_name_plural': 'Ответы на вопросы',
                'ordering': ['-created_at'],
            },
        ),
    ]