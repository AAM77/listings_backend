from django.db import models
from django.urls import reverse


class Post(models.Model):
    company = models.CharField(max_length=255)
    logo = models.CharField(max_length=255)
    new = models.BooleanField(default=False)
    featured = models.BooleanField(default=False)
    position = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    level = models.CharField(max_length=255)
    posted_at = models.CharField(max_length=255)
    contract = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    objects = models.Manager()

    class Meta:
        verbose_name = 'listing'
        verbose_name_plural = 'listings'

    def __str__(self):
        return f"{self.company}, {self.position}"

    # def get_absolute_url(self):
    #     return reverse("listing_detail", args=[str(self.id)])


class Tool(models.Model):
    name = models.CharField(max_length=255)
    listing = models.ManyToManyField(Post, blank=True, related_name='tools')

    class Meta:
        verbose_name = 'tool'
        verbose_name_plural = 'tools'
    
    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField(max_length=255)
    listing = models.ManyToManyField(Post, blank=True, related_name='languages')

    class Meta:
        verbose_name = 'language'
        verbose_name_plural = 'languages'
    
    def __str__(self):
        return self.name