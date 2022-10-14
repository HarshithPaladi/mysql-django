from django.urls import path
from . import views
app_name = 'App1'
urlpatterns = [
    path('', views.index, name='index'),
    #path('login/', views.user_login, name='login'),
    path('logout/',views.user_logout,name='logout'),
    path('create/',views.user_create,name='create'),
    path('show/',views.show,name='show'),
]
