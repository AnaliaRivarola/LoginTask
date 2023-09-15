from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from . import views

urlpatterns = [
    path('password_change/', views.PasswordChange.as_view(), name='password_change'),
    path('password_change/done/', views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('user_detail/<int:pk>/', views.UserDetail.as_view(), name='user_detail'),
    path('user_update/<int:pk>/', views.UserUpdate.as_view(), name='user_update'),
    path('user_delete/<int:pk>/', views.UserDelete.as_view(), name='user_delete'),
    path('signup/', CreateView.as_view(
        template_name='tasks/signup.html',
        form_class=UserCreationForm,
        success_url='/tasks/login/',  # Cambiado a '/tasks/login/'
    ), name='signup'),
    path('login/', LoginView.as_view(
        redirect_authenticated_user=True,
        template_name='tasks/login.html'
    ), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
