from django.contrib.auth.models import Group
from django.shortcuts import redirect, render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import GolfGroup
from .forms import GroupForm

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


class GroupList(TemplateView):
    template_name = "home.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["groups"] = GolfGroup.objects.all() # Here we are using the model to query the database for us.
        return context


@method_decorator(login_required, name='dispatch')
class GroupCreate(CreateView):
    model = GolfGroup
    form_class = GroupForm
    template_name = "group_create.html"
    success_url = "/"

class GroupUpdate(UpdateView):
    model = GolfGroup
    form_class = GroupForm
    template_name = "group_create.html"
    success_url = "/"

class GroupDelete(DeleteView):
    model = GolfGroup
    form_class = GroupForm
    template_name = "group_delete.html"
    success_url = "/"


