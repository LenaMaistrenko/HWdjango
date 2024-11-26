from django.urls import path
from . import views

urlpatterns = [
    path('', views.song_lyrics, {'lang_code': 'en'}, name='song_lyrics_en'),
    path('fr/', views.song_lyrics, {'lang_code': 'fr'}, name='song_lyrics_fr'),
    path('de/', views.song_lyrics, {'lang_code': 'de'}, name='song_lyrics_de'),
    path('es/', views.song_lyrics, {'lang_code': 'es'}, name='song_lyrics_es'),
]
