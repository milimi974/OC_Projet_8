from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
import json
from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
import tools
from product.models import Product
from .mocks import Products


def search(request):
    # Search products substitutions
    title = "Recherche d'aliment de substitution"

    substitutions = Products.all()
    product = Products.find(1)

    # pagination
    paginator = Paginator(substitutions, 12)
    page = request.GET.get('page')

    try:
        substitutions = paginator.page(page)
    except PageNotAnInteger:
        substitutions = paginator.page(1)
    except EmptyPage:
        substitutions = paginator.page(paginator.num_pages)


    pagination = tools.pagination(substitutions, 10)
    context = {
        'substitutions': substitutions,
        'product': product,
        'title': title,
        'pagination': pagination,
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



def save(request):
    if request.user.is_authenticated:
       pass

def terms(request):

    data_json = 'fail'
    if request.is_ajax:
        # get terms to search
        search = request.GET.get('term')
        if search:
            # search results into DB
            products = Product.objects.filter(name__contains=search)
            results = []
            # format data to return
            for product in products:
                product_json = {}
                product_json['label'] = product.name
                product_json['value'] = product.name
                results.append(product_json)
            # convert json answer
            data_json = json.dumps(results)

    mimetype = 'application/json'
    return HttpResponse(data_json, mimetype)