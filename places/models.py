from django.db import models
from django.utils.text import slugify


class Place(models.Model):
    name_ar = models.CharField(max_length=200)
    name_en = models.CharField(max_length=200)

    region_ar = models.CharField(max_length=200, blank=True)
    region_en = models.CharField(max_length=200, blank=True)

    description_ar = models.TextField(blank=True)
    description_en = models.TextField(blank=True)

    distance_info_ar = models.CharField(max_length=300, blank=True)
    distance_info_en = models.CharField(max_length=300, blank=True)

    latitude = models.DecimalField(max_digits=90, decimal_places=7, null=True, blank=True)
    longitude = models.DecimalField(max_digits=90, decimal_places=7, null=True, blank=True)

    main_image = models.ImageField(upload_to='places/main/', blank=True, null=True)

    slug = models.SlugField(max_length=220, unique=True, blank=True)

    # ترتيب يدوي
    order = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', 'id']

    def save(self, *args, **kwargs):
        if not self.slug:
            base = self.name_en or self.name_ar
            self.slug = slugify(base)[:200]
        super().save(*args, **kwargs)

    def google_maps_url(self):
        if self.latitude is None or self.longitude is None:
            return ""
        return f"https://www.google.com/maps?q={self.latitude},{self.longitude}"

    def __str__(self):
        return self.name_ar


class PlaceImage(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='places/gallery/')
    caption_ar = models.CharField(max_length=255, blank=True, verbose_name="تعليق (عربي)")
    caption_en = models.CharField(max_length=255, blank=True, verbose_name="Caption (English)")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name = "صورة المكان"
        verbose_name_plural = "صور المكان"

    def __str__(self):
        return f"Image for {self.place.name_en}"