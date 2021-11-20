from django.contrib.auth.models import Group
from django.shortcuts import redirect, render, get_object_or_404
from django.views import View
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from .models import GolfGroup, Profile
from .forms import GroupForm

# Create your views here.

def MemberView(request, pk):
    group = get_object_or_404(GolfGroup, id=request.POST.get('group_id'))
    current_member = False
    if group.members.filter(id=request.user.id).exists():
        group.members.remove(request.user)
        current_member = False
    else: 
        group.members.add(request.user)
        current_member = True

    return redirect('home')

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
            return redirect("/profile/new")
        else:
            context = {"form": form}
            return render(request, "registration/signup.html", context)


class ProfileView(DetailView):
    model = Profile
    template_name = "profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["groups"] = GolfGroup.objects.all()
        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        context["page_user"] = page_user
        return context

@method_decorator(login_required, name='dispatch')
class ProfileCreate(CreateView):
    model = Profile
    fields = [ 'bio', 'location', 'handicap', 'favorite_course', 'profile_img']
    template_name = "profile_create.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ProfileCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse('profile', kwargs={'pk': self.object.pk})

@method_decorator(login_required, name='dispatch')
class ProfileUpdate(UpdateView):
    model = Profile
    fields = [ 'bio', 'location', 'handicap', 'favorite_course', 'profile_img']
    template_name = "profile_update.html"
    
    def get_success_url(self):
        return reverse('profile', kwargs={'pk': self.object.pk})


class GroupList(TemplateView):
    model = GolfGroup
    template_name = "home.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["groups"] = GolfGroup.objects.all()
        return context


@method_decorator(login_required, name='dispatch')
class GroupCreate(CreateView):
    model = GolfGroup
    form_class = GroupForm
    template_name = "group_create.html"
    success_url = "/"

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
class GroupUpdate(UpdateView):
    model = GolfGroup
    form_class = GroupForm
    template_name = "group_update.html"
    success_url = "/"

@method_decorator(login_required, name='dispatch')
class GroupDelete(DeleteView):
    model = GolfGroup
    form_class = GroupForm
    template_name = "group_delete.html"
    success_url = "/"



