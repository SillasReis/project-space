from django.urls import path

from users.views import login, logout, signup


urlpatterns = [
    path('login', login, name='login'),
    path('signup', signup, name='signup'),
    path('logout', logout, name='logout'),
]
