# Generated by Django 3.0.5 on 2020-04-30 13:48

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, unique=True, verbose_name='Вид животного во множественном числе')),
                ('title_slug', models.SlugField(max_length=20, verbose_name='Вид животного для URL')),
                ('photo', models.ImageField(blank=True, upload_to='animals_photos', verbose_name='Фотография')),
            ],
            options={
                'verbose_name': 'Вид животного',
                'verbose_name_plural': 'Виды животных',
            },
        ),
        migrations.CreateModel(
            name='Breed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('breed', models.CharField(max_length=50, unique=True, verbose_name='Порода животного')),
                ('breed_slug', models.SlugField(blank=True, null=True, verbose_name='Порода животного для URL')),
                ('photo', models.ImageField(blank=True, upload_to='breed_photos', verbose_name='Фотография породы')),
                ('animal', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='animal_breed', to='pets.Animal', verbose_name='Вид животного')),
            ],
            options={
                'verbose_name': 'Порода животного',
                'verbose_name_plural': 'Породы животных',
            },
        ),
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Кличка')),
                ('age', models.IntegerField(validators=[django.core.validators.MaxValueValidator(50)], verbose_name='Возраст')),
                ('sex', models.CharField(choices=[('m', 'Мужской'), ('f', 'Женский')], default='m', max_length=1, null=True, verbose_name='Пол')),
                ('description', models.TextField(default=None, verbose_name='Информация о питомце')),
                ('date_registered', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата и время регистрации')),
                ('photo', models.ImageField(blank=True, upload_to='pets_photos', verbose_name='Фотография')),
                ('location', models.BooleanField(choices=[(True, 'В приюте'), (False, 'Вне приюта')], default=True, verbose_name='Местонахождение')),
                ('breed', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='pet_breed', to='pets.Breed', verbose_name='Порода животного')),
            ],
            options={
                'verbose_name': 'Питомец',
                'verbose_name_plural': 'Питомцы',
            },
        ),
    ]
