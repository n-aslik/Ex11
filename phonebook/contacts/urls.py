from django.urls import path
from contacts import views
from .views import  SearchResultsView
from django.contrib.auth.decorators import login_required





urlpatterns = [
    path('',login_required(views.worker_list),name='worker_list'),
    path('worker/create/',login_required(views.worker_create),name='worker_create'),
    path('worker/update/<int:id>/',views.worker_update,name='worker_update'),
    path('worker/delete/<int:id>/',views.worker_delete,name='worker_delete'),
    path('search/', SearchResultsView.as_view(), name='search'),
    path('login/',views.login_v,name='login'),
    path('logout/',views.logout_v,name='logout'),
   

    
]

     
   
