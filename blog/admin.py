from django.contrib import admin
from .models import Post

# This makes the 'Post' model show on the admin page
admin.site.register(Post)
