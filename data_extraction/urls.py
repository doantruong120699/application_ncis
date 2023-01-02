from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.ncis,name='issue_date'),
]