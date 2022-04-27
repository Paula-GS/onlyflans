import uuid
from django.db import models

class Flan(models.Model):
    flan_uuid = models.UUIDField()
    name = models.CharField(max_length=64)
    description = models.TextField()
    image_url = models.URLField()
    price = models.CharField(max_length=5)
    slug = models.SlugField()
    is_private = models.BooleanField()
    vegan = models.BooleanField(default=False)
    gluten_free = models.BooleanField(default=False)
    sugar_free = models.BooleanField(default=False)

class ContactForm(models.Model):
    contact_form_uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    customer_email = models.EmailField()
    customer_name = models.CharField(max_length=64)
    message = models.TextField()

class Recipe(models.Model):
    recipe_uuid = models.UUIDField()
    name = models.CharField(max_length=65)
    time_prep = models.CharField(max_length=3)
    time_cook = models.CharField(max_length=3)
    ingredients = models.TextField()
    preparation = models.TextField()
    image_url = models.URLField(default='link')
    
    
