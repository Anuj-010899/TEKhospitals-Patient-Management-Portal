from django.urls import path
from . import views

urlpatterns =[
    path('',views.home,name='home'),
    path('commoninfo',views.home,name='home'),
    path('commoninfo/add',views.addUser,name='add'),
    path('commoninfo/fetch',views.findUser,name='findUser'),
    
 
]