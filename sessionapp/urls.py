from django.urls import path
from .import views
app_name='sessionapp'
urlpatterns = [
    path('', views.input, name='input'),
    path('mul', views.mul, name='mul'),
    path('display',views.display,name='display')
]