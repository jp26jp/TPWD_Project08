import random

from django.db.models import Max
from django.shortcuts import render, redirect

from minerals.models import Mineral


def index(request):
    """
    View for the home page
    """
    minerals = Mineral.objects.all()
    return render(request, 'minerals/index.html', {'minerals': minerals})


def letter(request, letter):
    """
    View for the minerals that begin with the specified letter
    """
    minerals = Mineral.objects.filter(name__startswith=letter)
    context = {
        'letter': letter,
        'minerals': minerals
    }
    return render(request, 'minerals/index.html', context)


def group(request, group):
    """
    View for the minerals that belong to the specified group
    """
    group = group.split("-")[0]
    minerals = Mineral.objects.filter(group__startswith=group)
    context = {
        'group': group,
        'minerals': minerals
    }
    return render(request, 'minerals/index.html', context)


def search(request):
    """
    View for the minerals with a name that contains the specified query
    """
    term = request.GET.get('q')
    minerals = Mineral.objects.filter(name__icontains=term)
    return render(request, 'minerals/index.html', {'minerals': minerals})


def detail(request, slug):
    """
    View for the mineral that belongs to the specified slug
    """
    mineral = Mineral.objects.get(slug=slug)
    return render(request, 'minerals/detail.html', {'mineral': mineral})


def random_mineral(request):
    """
    View for displaying a random mineral
    """
    random_id = random.randint(1, Mineral.objects.count())
    mineral = Mineral.objects.get(pk=random_id)
    return redirect('minerals:detail', slug=mineral.slug)
