from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import MobileSuit, Weapons
from .forms import FuelingForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin



@login_required

def about(request):
    return render(request, 'about.html')

def ms_index(request):
    ms = MobileSuit.objects.filter(user=request.user)
    return render(request, 'index.html', {'ms': ms})

def ms_detail(request, ms_id):
    ms = MobileSuit.objects.get(id=ms_id)
    weapons_ms_doesnt_have = Weapons.objects.exclude(id__in = ms.weapons.all().values_list('id'))
    fueling_form = FuelingForm()
    return render(request, 'detail.html', {'ms': ms, 'fueling_form': fueling_form, 'weapons': weapons_ms_doesnt_have})

class MsCreate(LoginRequiredMixin, CreateView):
    model = MobileSuit
    fields = ['name', 'type', 'description', 'age']
    def form_valid(self, form):
        form.instance.user = self.request.user  
        return super().form_valid(form)

class MsUpdate(LoginRequiredMixin,UpdateView):
    model = MobileSuit
    fields = ['name', 'type', 'description', 'age']

class MsDelete(LoginRequiredMixin, DeleteView):
    model = MobileSuit
    success_url = '/ms/'

def add_fueling(request, ms_id):
    form = FuelingForm(request.POST)
    if form.is_valid():
        new_fueling = form.save(commit=False)
        new_fueling.mobile_suit_id = ms_id
        new_fueling.save()
    return redirect('ms-detail', ms_id=ms_id)

class WeaponCreate(LoginRequiredMixin, CreateView):
    model = Weapons
    fields = '__all__'

class WeaponList(LoginRequiredMixin, ListView):
    model = Weapons

class WeaponDetail(LoginRequiredMixin, DetailView):
    model = Weapons

class WeaponUpdate(LoginRequiredMixin, UpdateView):
    model = Weapons
    fields = ['name', 'color']

class WeaponDelete(DeleteView):
    model = Weapons
    success_url = '/weapons/'

def associate_weapon(request, ms_id, weapon_id):
    MobileSuit.objects.get(id=ms_id).weapons.add(weapon_id)
    return redirect('ms-detail', ms_id=ms_id)

def remove_weapon(request, ms_id, weapon_id):
    MobileSuit.objects.get(id=ms_id).weapons.remove(weapon_id)
    return redirect('ms-detail', ms_id=ms_id)

class Home(LoginView):
    template_name = 'home.html'
           
def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('ms-index') 
        else:
            error_message = 'Invalid sign up - try again'
            form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)