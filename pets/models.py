from django.db import models
from django.utils import timezone
from django.core import validators
from django.utils.text import slugify


class Animal(models.Model):
    """ Вид животного """
    title = models.CharField(max_length=20,
                             unique=True,
                             verbose_name='Вид животного во множественном числе')
    title_slug = models.SlugField(max_length=20,
                                  verbose_name='Вид животного для URL')
    photo = models.ImageField(upload_to='animals_photos',
                              blank=True,
                              verbose_name='Фотография')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Вид животного'
        verbose_name_plural = 'Виды животных'


class Breed(models.Model):
    """ Порода животного """
    breed = models.CharField(max_length=50,
                             unique=True,
                             verbose_name="Порода животного")
    breed_slug = models.SlugField(max_length=50,
                                  verbose_name='Порода животного для URL',
                                  null=True,
                                  blank=True,
                                  default=None)
    animal = models.ForeignKey(Animal,
                               on_delete=models.CASCADE,
                               related_name='animal_breed',
                               verbose_name='Вид животного',
                               default=None)
    photo = models.ImageField(upload_to='breed_photos',
                              blank=True,
                              verbose_name='Фотография породы')

    def __str__(self):
        return f'{self.breed} ({self.animal})'

    class Meta:
        verbose_name = 'Порода животного'
        verbose_name_plural = 'Породы животных'


class Pet(models.Model):
    """ Данные о животном """
    LOCATION_CHOICES = (
        (True, 'В приюте'),
        (False, 'Вне приюта')
    )

    SEX_CHOICES = (
        ('m', 'Мужской'),
        ('f', 'Женский')
    )

    name = models.CharField(max_length=100,
                            verbose_name='Кличка')
    breed = models.ForeignKey(Breed,
                              on_delete=models.CASCADE,
                              related_name='pet_breed',
                              verbose_name='Порода животного',
                              default=None)
    age = models.IntegerField(verbose_name="Возраст",
                              validators=[validators.MaxValueValidator(50)])
    sex = models.CharField(choices=SEX_CHOICES,
                           max_length=1,
                           verbose_name='Пол',
                           null=True,
                           default='m')
    description = models.TextField(verbose_name='Информация о питомце',
                                   default=None)
    date_registered = models.DateTimeField(default=timezone.now,
                                           verbose_name='Дата и время регистрации')
    photo = models.ImageField(upload_to='pets_photos',
                              blank=True,
                              verbose_name='Фотография')
    location = models.BooleanField(choices=LOCATION_CHOICES,
                                   default=True,
                                   verbose_name='Местонахождение')

    def __str__(self):
        return f'{self.breed} по кличке {self.name}'

    class Meta:
        verbose_name = 'Питомец'
        verbose_name_plural = 'Питомцы'
