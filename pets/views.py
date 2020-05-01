from django.shortcuts import get_list_or_404, get_object_or_404, render
from django.views.generic import ListView
from django.views.generic.detail import DetailView

from .models import Animal, Breed, Pet


class AnimalsListView(ListView):
    """ Выводит все виды животных в приюте """
    queryset = Animal.objects.all().order_by('title')
    context_object_name = 'animals'
    template_name = 'pets/animals.html'


class BreedListView(ListView):
    """ Выводит все породы животных заданного вида """
    context_object_name = 'breeds'
    template_name = 'pets/breeds.html'

    def get_queryset(self):
        return get_list_or_404(Breed.objects.filter(animal__title_slug=self.kwargs['animal']).order_by('breed'))

    def get_context_data(self, **kwargs):
        context = super(BreedListView, self).get_context_data(**kwargs)
        context['current_animal'] = Animal.objects.get(title_slug=self.kwargs['animal'])
        return context


class PetListView(ListView):
    """ Выводит всех питомцев заданной породы  """
    context_object_name = 'pets'
    template_name = 'pets/pets.html'

    def get_queryset(self):
        return get_list_or_404(Pet.objects.filter(breed__animal_id=self.kwargs['pk'],
                                                  breed__breed_slug=self.kwargs['breed'],
                                                  location=True).order_by('name'))

    def get_context_data(self, **kwargs):
        context = super(PetListView, self).get_context_data(**kwargs)
        context['current_animal'] = Animal.objects.get(id=self.kwargs['pk'])
        context['current_breed'] = Breed.objects.get(breed_slug=self.kwargs['breed'])
        return context


class PetDetailView(DetailView):
    """ Выводит подробную информацию о питомце """
    model = Pet
    template_name = 'pets/pet_detail.html'


def about_info(request):
    """ Выводит информацию о питомнике """
    total_animals = Animal.objects.all().count()
    total_breeds = Breed.objects.all().count()
    total_pets = Pet.objects.all().filter(location=True).count()

    return render(request,
                  'about/about.html',
                  {'total_animals': total_animals,
                   'total_breeds': total_breeds,
                   'total_pets': total_pets})


def contact_info(request):
    """ Выводит контакнтую информацию """
    return render(request,
                  'contact/contact.html')
