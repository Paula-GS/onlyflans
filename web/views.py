from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Flan, ContactForm, Recipe
from .forms import ContactFormForm
from .forms import ContactFormModelForm
from django.contrib.auth.decorators import login_required


def index(request):
    public_flans = Flan.objects.filter(is_private=False)

    return render(
        request,
        'index.html', 
        {
            'public_flans': public_flans
        })


def about(request):
    return render(request, 'about.html', {})

@login_required
def welcome(request):
    private_flans = Flan.objects.filter(is_private=True)

    return render(
        request,
        'welcome.html',
        {
        'private_flans': private_flans
        })


def contacto(request):
    if request.method == 'POST':
        #crea una instancia de formulario y la llena con información desde el request:
        form = ContactFormModelForm(request.POST)
        #revisa si es válido
        if form.is_valid():
            #procesa los datos en form.cleaned_data como se solicitó
            #...
            contact_form = ContactForm.objects.create(**form.cleaned_data)

            #redirecciona a una nueva URL (no olvides completar con la URL a la que quieres que vaya):
            return HttpResponseRedirect('/exito')
    # si es un GET (o cualquier otro método) creará un formulario en blanco
    else:
        form = ContactFormModelForm()

    return render(request, 'contactus.html', {'form': form})


def exito(request):
    return render(request, 'success.html', {})

#def logout(request):
#    return render(request, './registration/logout.html')


@login_required
def special(request):
    vegan = Flan.objects.filter(vegan=True)
    sugar_free = Flan.objects.filter(sugar_free=True)
    gluten_free = Flan.objects.filter(gluten_free=True)

    return render(
        request,
        'special.html',
        {
        'sugar_free': sugar_free,
        'gluten_free': gluten_free,
        'vegan': vegan
        })

@login_required
def recipe(request):
    recipe = Recipe.objects.all()
    return render(
        request,
        'recipes.html',
        {
            'recipe': recipe
        })