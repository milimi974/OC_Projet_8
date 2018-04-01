from django.http import HttpResponseForbidden, HttpResponse
from django.shortcuts import render
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout
)

# Create your views here.
from django.views.generic import CreateView

from .forms import UserRegisterForm, UserLoginForm


class RegisterUserView(CreateView):
    form_class = UserRegisterForm
    template_name =  "account/register.html"

    def dispatch(self, request, *args, **kwargs):

        if request.user.is_authenticated:
            return HttpResponseForbidden()
        return super(RegisterUserView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):

        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.save()

        return HttpResponse('User registered')

# login view
def login_view(request):
    title = "login"
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        login(request, user)
    context = {"form":form, "title": title}
    return render(request, 'account/form.html', context)

# logout view
def logout_view(request):
    return render(request, 'form.html', {})

# register view
def register_view(request):
    return render(request, 'form.html', {})