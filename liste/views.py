from django.shortcuts import render, redirect

from .models import Liste
from .forms import ListeForm

from django.contrib import messages



# Create your views here.
def home(request):
    if request.method == 'POST':
        form = ListeForm(request.POST or None)

        if form.is_valid():
            form.save()
            all_items = Liste.objects.all
            messages.success(request, ('L\'article a ete rajoute dans votre liste de course, felicitation !'))
            return render(request, 'home.html', {'all_items' : all_items})

        else:
            all_items = Liste.objects.all
            return render(request, 'home.html', {'all_items' : all_items})

def delete(request, liste_id):
    item = Liste.objects.get(pk=liste_id)
    item.delete()
    messages.success(request, ('L\'article a ete supprime'))
    return redirect('home')

def barrer(request, liste_id):
    item = Liste.objects.get(pk=liste_id)
    item.completed = True
    item.save()
    return redirect('home')

def debarrer(request, liste_id):
    item = Liste.objects.get(pk=liste_id)
    item.completed = False
    item.save()
    return redirect('home')


def edit(request, liste_id):
    if request.method == 'POST':
        item = Liste.objects.get(pk=liste_id)

        form = ListeForm(request.POST or None, instance=item)

        if form.is_valid():
            form.save()
            messages.success(request, ('L\'article a ete modifie, felicitation !'))
            return redirect('home')

        else:
            item = Liste.objects.get(pk=liste_id)
            return render(request, 'edit.html', {'item' : item})
