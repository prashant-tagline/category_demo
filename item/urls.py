
from django.urls import  path
from . import views
urlpatterns = [
    path('getsubcategory', views.get_subcategory),
    path('', views.Home.as_view()),
    path('<slug:slug>', views.ItemListView.as_view(), name="items"),
]   