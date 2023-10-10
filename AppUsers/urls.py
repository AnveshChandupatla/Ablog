from django.urls import path
from .views import UserRegisterView, UserEditView, ShowProfilePageView,EditProfilePageView, CreateProfilePageView
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('edit_profile/', UserEditView.as_view(), name='edit_profile'),
    path('<int:pk>/profile/',ShowProfilePageView.as_view(), name='show_profile_page'),
    path('<int:pk>/edit_profile_page/',EditProfilePageView.as_view(), name='edit_profile_page'),
    path('<int:pk>/create_profile_page/',CreateProfilePageView.as_view(), name='create_profile'),
    # path('changepassword/', PasswordsChangeView.as_view(), name='change_password'),
    # path('password/', auth_views.as_view(template_name='registration/change_password.html')),

    

]