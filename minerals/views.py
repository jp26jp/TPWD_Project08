from django.shortcuts import render

from minerals.models import Mineral


def index(request):
    minerals = Mineral.objects.all()
    return render(request, 'minerals/index.html', {'minerals': minerals})


def letter(request, letter):
    # TODO: find a way to bold the selected letter
    minerals = Mineral.objects.filter(name__startswith=letter)
    context = {
        'letter': letter,
        'minerals': minerals
    }
    return render(request, 'minerals/index.html', context)


def search(request):
    term = request.GET.get('q')
    minerals = Mineral.objects.filter(name__icontains=term)
    return render(request, 'minerals/index.html', {'minerals': minerals})


def detail(request, slug):
    mineral = Mineral.objects.get(slug=slug)
    return render(request, 'minerals/detail.html', {'mineral': mineral})
