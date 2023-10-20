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
        'texto1' : "1",
        'texto2' : "2",
        'texto3' : "3",
        'texto4' : "4",
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
        'texto1' : "1",
        'texto2' : "2",
        'texto3' : "3",
        'texto4' : "4",
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
        'musica2':"Bon Jovi",
        'musica3':"The human league",
        'musica4':"Scorpions",
        'texto1' : "1",
        'texto2' : "2",
        'texto3' : "3",
        'texto4' : "4",
        'imagen1':'imagenes/demi.png',
        'imagen2':'imagenes/miley.png',
        'imagen3':'imagenes/katy.png',
        'imagen4':'imagenes/britney.png',
    }
    return render(request,'templatesMusica/musica.html',data)