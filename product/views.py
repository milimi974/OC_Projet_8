from django.shortcuts import render

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