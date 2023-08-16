from django.urls import path,include
from.import views
urlpatterns = [
    path('',views.index,name = 'index'),
    path('getquery',views.getquery,name = "getquery"),
    path("sortdata",views.sortdata,name="sortdata")
]