from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.
from .mocks import Products


def search(request):
    # Search products substitutions
    title = "Recherche d'aliment de substitution"
    substitutions = Products.all()
    product = Products.find(1)

    context = {
        'substitutions': substitutions,
        'product': product,
        'title': title,
    }
    return render(request, 'product/search.html',context)


def show(request, id):
    """
    Display product
    :param request:
    :param id: product id
    :return: show view
    """
    title = "Aliments de substitution"
    product = Products.find(id)

    context = {
        'product':product,
        'title': title,
    }
    return render(request, 'product/show.html', context)

@login_required(login_url='/login/')
def list(request):
    # user products substitutions
    title = "Mes aliments de substitution"
    substitutions = Products.all()
    product = Products.find(1)

    context = {
        'substitutions': substitutions,
        'product': product,
        'title': title,
    }
    return render(request, 'product/user_list.html', context)

def save(request):
    if request.user.is_authenticated:
       pass