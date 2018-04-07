import json

from django.contrib.auth.decorators import login_required
from django.core.paginator import PageNotAnInteger, EmptyPage, Paginator
from django.http import HttpResponse

from django.shortcuts import render, redirect
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout
)

# Create your views here.

import tools
from account.models import UserProduct
from product.models import Product
from .forms import UserRegisterForm, UserLoginForm
# from product.mocks import  Product

# login view
def login_view(request):

    if request.user.is_authenticated:
        return redirect("/")
    next = request.GET.get('next')
    title = "Connexion"
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        login(request, user)
        if next:
            return redirect(next)
        return redirect("/")

    context = {"form":form, "title": title}
    return render(request, 'account/form.html', context)

# logout view
def logout_view(request):
    # redirect homepage if already disconnected
    if not request.user.is_authenticated:
        return redirect("/")
    # Disconnect user
    logout(request)
    return render(request, 'account/logout.html')

# register view
def register_view(request):
    title = "inscription"
    form = UserRegisterForm(request.POST or None)
    # get reference to page to redirect after connection
    next = request.GET.get('next')

    # Create user if clean form data
    if form.is_valid():
        user = form.save(commit=False)
        pwd = form.cleaned_data.get('password')
        user.set_password(pwd)
        user.save()
        login(request, user)
        if next:
            return redirect(next)
        return redirect("/")

    context = {"form": form, "title": title}
    return render(request, 'account/form.html', context)

# user profile view
def profile_view(request):
    title = "Profil"
    return render(request, 'account/profile.html', {"title": title})

@login_required(login_url='/login/')
def list(request):
    # user product substitutions
    title = "Mes aliments de substitution"
    #substitutions = Product.all()
    user_product = UserProduct.objects.all()

    # pagination
    paginator = Paginator(user_product, 12)
    page = request.GET.get('page')

    try:
        user_product = paginator.page(page)
    except PageNotAnInteger:
        user_product = paginator.page(1)
    except EmptyPage:
        user_product = paginator.page(paginator.num_pages)

    pagination = tools.pagination(user_product, 10)

    context = {
        'user_product': user_product,
        'title': title,
        'pagination': pagination
    }

    return render(request, 'account/user_list.html', context)


def save(request):
    data_json = {'status': 'error','message':'Produit déjà dans vos favoris.'}
    if request.user.is_authenticated:

        product_id =  request.POST.get('id')
        substitution_id =  request.POST.get('sub_id')
        # if ids exists
        if product_id and substitution_id:
            # if substitution product already exist
            sub = Product.objects.get(id=substitution_id)
            if sub:
                qs = UserProduct.objects.get(product_id=product_id)
                if not qs:
                    qs = UserProduct.objects.create(product_id=product_id)
                qs.substitution.add(sub)

    # convert json answer
    data_json = json.dumps(data_json)
    mimetype = 'application/json'
    return HttpResponse(data_json, mimetype)