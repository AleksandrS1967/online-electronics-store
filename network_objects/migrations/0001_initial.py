# Generated by Django 5.1.1 on 2024-09-14 11:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name',
                 models.CharField(help_text='Введите название продукта', max_length=255, verbose_name='Название')),
                ('model',
                 models.TextField(blank=True, help_text='Введите название модели', null=True, verbose_name='Модель')),
                ('release_date', models.DateTimeField(blank=True, null=True, verbose_name='дата выхода')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
            },
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Завод', 'Завод'), ('Розничная сеть', 'Сеть'),
                                                   ('индивидуальный предприниматель', 'Предприниматель')],
                                          help_text='Выберите тип поставщика', verbose_name='тип поставщика')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='email')),
                ('country', models.TextField(blank=True, null=True, verbose_name='Страна')),
                ('city', models.TextField(blank=True, null=True, verbose_name='Город')),
                ('street', models.TextField(blank=True, null=True, verbose_name='Улица')),
                ('house_number', models.TextField(blank=True, null=True, verbose_name='Номер дома')),
                ('debt', models.FloatField(blank=True, null=True, verbose_name='Задолженность')),
                ('release_date', models.DateTimeField(auto_now=True, null=True, verbose_name='дата создания')),
                ('products', models.ManyToManyField(to='network_objects.product', verbose_name='Продукт')),
                ('purveyor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT,
                                               to='network_objects.supplier', verbose_name='Поставщик')),
            ],
            options={
                'verbose_name': 'Поставщик',
                'verbose_name_plural': 'Поставщики',
            },
        ),
    ]
