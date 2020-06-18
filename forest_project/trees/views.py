from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Tree
from django.urls import reverse_lazy

# Create your views here.

class TreeListView(ListView):
    template_name = 'tree_list.html'
    model = Tree

class TreeDetailView(DetailView):
    template_name = 'tree_details.html'
    model = Tree

class TreeCreateView(CreateView):
    template_name = 'tree_create.html'
    model = Tree
    fields = ['name', 'planter', 'description']
    success_url = reverse_lazy('tree_list')

class TreeUpdateView(UpdateView):
    template_name = 'tree_update.html'
    model = Tree
    fields = ['name', 'description']
    success_url = reverse_lazy('tree_list')

class TreeDeleteView(DeleteView):
    template_name = 'tree_delete.html'
    model = Tree
    success_url = reverse_lazy('tree_list')
