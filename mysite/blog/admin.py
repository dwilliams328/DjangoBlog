from django.contrib import admin

# Import and register model to make it visible on the admin page.
from .models import Post

admin.site.register(Post)