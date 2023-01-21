from django.urls import path

from gallery.views import image, index


urlpatterns = [
    path('', index, name='index'),
    path('image/', image, name='image')
]
