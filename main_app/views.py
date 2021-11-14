from django.contrib.auth.models import Group
from django.shortcuts import redirect, render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView
from .models import GolfGroup

# Create your views here.

class Signup(View):
    def get(self, request):
        form = UserCreationForm()
        context = {"form": form}
        return render(request, "registration/signup.html", context)
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("/")
        else:
            context = {"form": form}
            return render(request, "registration/signup.html", context)


class Profile(TemplateView):
    template_name = "profile.html"


# # @method_decorator(login_required, name='dispatch')
# class Home(TemplateView):
#     template_name = "home.html"


# class GroupList(TemplateView):
#     template_name = "groups.html"

#     def get_context_data(self, **kwargs):
#         print(self)
#         context = super().get_context_data(**kwargs)
#         context["groups"] = GolfGroup.objects.all()
#         print(context)
#         return context

class GroupList(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["groups"] = GolfGroup.objects.all() # Here we are using the model to query the database for us.
        return context


    


