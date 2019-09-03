from django.shortcuts import render

from minerals.models import Mineral


def index(request):
    minerals = Mineral.objects.all()
    return render(request, 'minerals/index.html', {'minerals': minerals})


def detail(request, slug):
    mineral = Mineral.objects.get(slug=slug)
    return render(request, 'minerals/detail.html', {'mineral': mineral})
