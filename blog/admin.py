from django.contrib import admin
from .models import Post

#Aby nasz model był widoczny w panelu admina,
# musimy go zarejestrować za pomocą polecenia
admin.site.register(Post)
