from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.
from .mocks import Products


def search(request):
    # Search products substitutions
    substitutions = Products.all()
    product = Products.find(1)
    return render(request, 'product/search.html',{'substitutions': substitutions, 'product': product})


def show(request, id):
    """
    Display product
    :param request:
    :param id: product id
    :return: show view
    """
    product = Products.find(id)
    return render(request, 'product/show.html', {'product':product})

@login_required(login_url='/login/')
def list(request):
    # user products substitutions

    substitutions = Products.all()
    product = Products.find(1)
    return render(request, 'product/user_list.html',{'substitutions': substitutions, 'product': product})