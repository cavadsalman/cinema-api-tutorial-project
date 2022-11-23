from django.urls import path
from . import views
from rest_framework.authtoken import views as auth_views

urlpatterns = [
    path('register/', views.RegisterAV.as_view(), name='register'),
    path('say-my-name/', views.say_my_name),
    path('login/', auth_views.obtain_auth_token),
    path('logout/', views.logout_view)
    # path('login/', views.login_view)
]
