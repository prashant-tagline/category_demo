
from django.urls import  path
from . import views
urlpatterns = [
    path('getsubcategory', views.get_subcategory),
    path('getcategory', views.get_category),
    path('', views.Home.as_view()),
    path('<slug:sub_category>', views.ItemListView.as_view(), name="items"),
]