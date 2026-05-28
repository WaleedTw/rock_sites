from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Place

def place_list(request):
    q = request.GET.get("q", "").strip()

    # ✅ IMPORTANT: sort by order first (then created_at)
    places = Place.objects.all().order_by("order", "-created_at")

    if q:
        places = places.filter(
            Q(name_ar__icontains=q) |
            Q(name_en__icontains=q) |
            Q(region_ar__icontains=q) |
            Q(region_en__icontains=q)
        )

    return render(request, "places/place_list.html", {"places": places, "q": q})

def place_detail(request, slug):
    place = get_object_or_404(Place.objects.prefetch_related('images'), slug=slug)
    return render(request, "places/place_detail.html", {"place": place})