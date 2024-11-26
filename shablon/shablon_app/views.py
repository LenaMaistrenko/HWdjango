from django.shortcuts import render


# Функція для відображення тексту пісні на різних мовах
def song_lyrics(request, lang_code='en'):
    song_texts = {
        'en': """
            We are the champions, my friends 
            And we’ll keep on fighting till the end
        """,
        'de': """
            Wir sind die Champions, meine Freunde
            Und wir werden bis zum Ende kämpfen
        """,
        'fr': """
            Nous sommes les champions, mes amis
            Et nous continuerons à nous battre jusqu'à la fin
        """,
        'es': """
            Somos los campeones, mis amigos
            Y seguiremos luchando hasta el final
        """
    }


    signatures = {
        'en': "Queen, We are the champions",
        'de': "Queen, Wir sind die Champions",
        'fr': "Queen, Nous sommes les champions",
        'es': "Queen, Somos los campeones"
    }


    text = song_texts.get(lang_code, song_texts['en'])
    signature = signatures.get(lang_code, signatures['en'])

    return render(request, 'song.html', {'text': text, 'signature': signature})
