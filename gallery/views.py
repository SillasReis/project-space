from django.contrib import messages
from django.shortcuts import redirect, render, get_object_or_404

from gallery.models import Photo


def index(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Faça o login para ver as imagens.')
        return redirect('login')

    photos = Photo.objects.order_by("-created_at").filter(is_published=True)
    return render(request, "gallery/index.html", {"photos": photos})


def image(request, photo_id):
    if not request.user.is_authenticated:
        messages.error(request, 'Faça o login para ver as imagens.')
        return redirect('login')

    photo = get_object_or_404(Photo, pk=photo_id)
    return render(request, "gallery/image.html", {"photo": photo})


def search(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Faça o login para ver as imagens.')
        return redirect('login')
    photos = Photo.objects.filter(is_published=True).order_by("-created_at")
    
    if "search" in request.GET:
        search_query = request.GET["search"]
        if search_query:
            photos = photos.filter(name__icontains=search_query)

    return render(request, "gallery/index.html", {"photos": photos})
