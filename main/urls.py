from django.urls import path
from . import views

urlpatterns =[
    path('',views.home,name='home'),
    path('commoninfo',views.home,name='home'),
    path('commoninfo/add',views.addUserInfo,name='add'),
    path('commoninfo/fetch',views.fetchUserInfo,name='findUser'),
    
 
]