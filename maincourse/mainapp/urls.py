from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name="home"),
    path('home/', views.homepage, name="home"),
    path('words_list/', views.dictionary, name='dictionary'),
    path('add_word/', views.add_word, name='add_word'),
]
