from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    #path('admin/', admin.site.urls),
    path('tasks/', include('tasks.urls')),
    path('login/', views.custom_login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
]
