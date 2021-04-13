from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView 
from .models import Craft
from django.views.generic import ListView

# Create your views here.


    
def about(request):
  return render(request, 'about.html')

def crafts_index(request):
  crafts = Craft.objects.all()
  return render(request, 'crafts/index.html', { 'crafts': crafts })

def crafts_detail(request, craft_id):
  craft = Craft.objects.get(id=craft_id)
  return render(request, 'crafts/detail.html', { 'craft': craft })

class CraftCreate(CreateView):
  model = Craft
  fields = '__all__'

class CraftUpdate(UpdateView):
  model = Craft
  fields = []

class CraftDelete(DeleteView):
  model = Craft
  success_url = '/'
class Index(ListView):
    model = Craft
    fields = ['name']