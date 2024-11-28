from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Animal
from django.shortcuts import redirect
from .forms import AnimalForm
from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponseRedirect
from .models import Animal
from .forms import AnimalForm


def animal_list(request):
    animals = Animal.objects.filter(available=True).order_by('-created_at')
    paginator = Paginator(animals, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if request.method == 'POST':
        form = AnimalForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('animal-list')
    else:
        form = AnimalForm()

    return render(request, 'animals/animal_list.html', {'page_obj': page_obj, 'form': form})


def animal_edit(request, pk):
    animal = get_object_or_404(Animal, pk=pk)
    if request.method == "POST":
        form = AnimalForm(request.POST, request.FILES, instance=animal)
        if form.is_valid():
            form.save()
            return redirect('animal-list')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def animal_delete(request, pk):
    animal = get_object_or_404(Animal, pk=pk)
    if request.method == "POST":
        animal.delete()
        return redirect('animal-list')
