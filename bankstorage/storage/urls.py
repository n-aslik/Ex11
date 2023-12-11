from django.urls import path
from storage import views
from .views import UserSearchResultsView,IncomingSearchResultsView,OutcomingSearchResultsView,BranchSearchResultsView,BranchAccessSearchResultsView,StorageSearchResultsView
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('user/',login_required(views.user_list),name='user_list'),
    path('user/update/<int:id>/',views.user_update,name='user_update'),
    path('user/delete/<int:id>/',views.user_delete,name='user_delete'),

    
    
    path('incoming/',login_required(views.incoming_list),name='incoming_list'),
    path('incoming/create/',login_required(views.incoming_create),name='incoming_create'),
    path('incoming/update/<int:id>/',views.incoming_update,name='incoming_update'),
    path('incoming/delete/<int:id>/',views.incoming_delete,name='incoming_delete'),
    
    path('outcoming/',login_required(views.outcoming_list),name='outcoming_list'),
    path('outcoming/create/',login_required(views.outcoming_create),name='outcoming_create'),
    path('outcoming/update/<int:id>/',views.outcoming_update,name='outcoming_update'),
    path('outcoming/delete/<int:id>/',views.outcoming_delete,name='outcoming_delete'),
    
    path('branch/',login_required(views.branch_list),name='branch_list'),
    path('branch/create/',login_required(views.branch_create),name='branch_create'),
    path('branch/update/<int:id>/',views.branch_update,name='branch_update'),
    path('branch/delete/<int:id>/',views.branch_delete,name='branch_delete'),
    
    path('branch_access/',login_required(views.branch_access_list),name='branch_access_list'),
    path('branch_access/create/', views.branch_access_create, name='branch_access_create'),
    path('branch_access/update/<int:id>/',views.branch_access_update,name='branch_access_update'),
    path('branch_access/delete/<int:id>/',views.branch_access_delete,name='branch_access_delete'),
    
    path('storage/',login_required(views.storage_list),name='storage_list'),
    path('storage/create/',login_required(views.storage_create),name='storage_create'),
    path('storage/update/<int:id>/',views.storage_update,name='storage_update'),
    path('storage/delete/<int:id>/',views.storage_delete,name='storage_delete'),

    
    
    path('',views.login_view,name='login'),
    path('logout/',views.logout_view,name='logout'),
    path('login/?next=/home/',views.home,name='home'),
    
    path('reestr/',views.reestr, name='reestr'),
    
    path('user_search/', UserSearchResultsView.as_view(), name='user_search'),
    path('incoming_search/', IncomingSearchResultsView.as_view(), name='incoming_search'),
    path('outcoming_search/', OutcomingSearchResultsView.as_view(), name='outcoming_search'),
    path('branch_search/', BranchSearchResultsView.as_view(), name='branch_search'),
    path('branch_access_search/', BranchAccessSearchResultsView.as_view(), name='branch_access_search'),
    path('storage_search/', StorageSearchResultsView.as_view(), name='storage_search'),
    
]

