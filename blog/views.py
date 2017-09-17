from django.shortcuts import render
from django.utils import timezone
from .models import Post

# kropka po from oznaca bieżący katalog/aplikację
# Jako że pliki views.py i models.py są
#  w tym katalogu, możemy użyć po prostu . i
# nazwy pliku (bez .py).

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts':posts})
