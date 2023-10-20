from django.shortcuts import render

# Create your views here.
def musica(request):
    return render(request,'templatesMusica/musica.html')

def pop(request):
    data={
        "titulo":"Cantantes POP ",
        'musica1':"Demi Lovato",
        'musica2':"Miley Cyrus",
        'musica3':"Katy Perry",
        'musica4':"Britney Spears",
        'texto1' : "N° 1",
        'texto2' : "N° 2",
        'texto3' : "N° 3",
        'texto4' : "N° 4",
        'imagen1':'imagenes/demi.png',
        'imagen2':'imagenes/miley.png',
        'imagen3':'imagenes/katy.png',
        'imagen4':'imagenes/britney.png',
    }
    return render(request,'templatesMusica/musica.html',data)

def rock(request):
    data={
        "titulo":"Bandas Rock",
        'musica1':"Queen",
        'musica2':"The Rolling Stones",
        'musica3':"Black Sabbath",
        'musica4':"Pink Floyd",
        'texto1' : "N° 1",
        'texto2' : "N° 2",
        'texto3' : "N° 3",
        'texto4' : "N° 4",
        'imagen1':'imagenes/queen.png',
        'imagen2':'imagenes/rolling.png',
        'imagen3':'imagenes/black.png',
        'imagen4':'imagenes/pink.png',
    }
    return render(request,'templatesMusica/musica.html',data)

def electro(request):
    data={
        "titulo":"Bandas electronica ",
        'musica1':"Daft Punk",
        'musica2':"Twenty One Pilots",
        'musica3':"Despeche Mode",
        'musica4':"Bjork",
        'texto1' : "N° 1",
        'texto2' : "N° 2",
        'texto3' : "N° 3",
        'texto4' : "N° 4",
        'imagen1':'imagenes/daft.png',
        'imagen2':'imagenes/one.png',
        'imagen3':'imagenes/despeche.png',
        'imagen4':'imagenes/bjork.png',
    }
    return render(request,'templatesMusica/musica.html',data)