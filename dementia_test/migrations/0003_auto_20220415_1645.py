# Generated by Django 3.2.9 on 2022-04-15 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dementia_test', '0002_auto_20220414_0008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='answer_value',
            field=models.CharField(blank=True, default='-', max_length=255, null=True, verbose_name='Значение ответа'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='image',
            field=models.ImageField(blank=True, default='', null=True, upload_to='answer/', verbose_name='Изображение'),
        ),
    ]