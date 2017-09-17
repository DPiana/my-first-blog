from django import forms #importujemy formularze django

from .models import Post #importujemy nasz model posta

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)
        # wskazujemy ktore pola Postu pojawia sie w formularzu
        #np. data bedzie uzupelniana automatycznie