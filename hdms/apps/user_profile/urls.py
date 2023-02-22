from django.urls import path, include
from . import views
app_name = 'apps.user_profile'
urlpatterns = [
    path('', views.dashboard, name='dashboard'),
]
