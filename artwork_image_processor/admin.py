from django.contrib import admin
from .models import Image

# Register your models here.

# this allows us to modify our models from the browser
# $ python manage.py createsuperuser
admin.site.register(Image)
