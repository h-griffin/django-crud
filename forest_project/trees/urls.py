from django.urls import path
from .views import TreeListView, TreeDetailView, TreeCreateView, TreeUpdateView, TreeDeleteView  #.views because file in same folder just moving over

urlpatterns=[
    path('', TreeListView.as_view(), name='tree_list'),
    path('trees/<int:pk>/', TreeDetailView.as_view(), name='tree_details'),
    path('trees/new/', TreeCreateView.as_view(), name='tree_create'),
    path('trees/<int:pk>/edit', TreeUpdateView.as_view(), name='tree_update'),
    path('trees/<int:pk>/delete/', TreeDeleteView.as_view(), name='tree_delete')
]