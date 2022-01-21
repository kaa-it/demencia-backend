# Generated by Django 3.2.9 on 2022-01-21 19:41

from django.db import migrations
import url_or_relative_url_field.fields


class Migration(migrations.Migration):

    dependencies = [
        ('demencia', '0004_newsarticle_sub_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leftmenuelement',
            name='url',
            field=url_or_relative_url_field.fields.URLOrRelativeURLField(max_length=250, verbose_name='Ссылка'),
        ),
        migrations.AlterField(
            model_name='mainmenuelement',
            name='url',
            field=url_or_relative_url_field.fields.URLOrRelativeURLField(max_length=250, verbose_name='Ссылка'),
        ),
    ]
