from django.contrib import admin
from .models import Animal, Breed, Pet


@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ('title', 'title_slug')
    prepopulated_fields = {'title_slug': ('title',)}
    ordering = ('title',)


@admin.register(Breed)
class BreedAdmin(admin.ModelAdmin):
    list_display = ('animal', 'breed')
    ordering = ('animal', 'breed')
    raw_id_fields = ('animal',)
    prepopulated_fields = {'breed_slug': ('breed',)}


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    # list_display = ('name', 'breed')
    raw_id_fields = ('breed',)
