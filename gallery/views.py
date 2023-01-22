from django.shortcuts import render, get_object_or_404

from gallery.models import Photo


def index(request):
    photos = Photo.objects.order_by("-created_at").filter(is_published=True)
    return render(request, "gallery/index.html", {"photos": photos})


def image(request, photo_id):
    photo = get_object_or_404(Photo, pk=photo_id)
    return render(request, "gallery/image.html", {"photo": photo})


def search(request):
    photos = Photo.objects.filter(is_published=True).order_by("-created_at")
    
    if "search" in request.GET:
        search_query = request.GET["search"]
        if search_query:
            photos = photos.filter(name__icontains=search_query)

    return render(request, "gallery/index.html", {"photos": photos})
