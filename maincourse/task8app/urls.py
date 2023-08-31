from django.urls import path
from . import views

urlpatterns = [
    path('reg/', views.registration, name='registration'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('notes/', views.show_notes, name='notes'),
    path('add_note/', views.add_note, name='add_note'),
]
