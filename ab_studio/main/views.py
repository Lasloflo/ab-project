from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import ContactForm
from .models import *
import requests

menu = {
    'Home': 'main:home',
    'About': 'main:about',
    'Services': 'main:services',
    'Gallery': 'main:gallery',
    'Video': 'main:video',
    'Blog': 'main:blog',
    'Contact': 'main:contact',

}
# Create your views here.
def index(request):
    content = PhotoInHomePage.objects.all()

    context = {
        'title': 'Home',
        'menu': menu,
        'photos': content
    }
    return render(request, 'main/index.html', context=context)



def about(request):
    pass

def services(request):
    pass

def show_album(request, album_slug):
    album = Album.objects.get(slug=album_slug)
    photos = PhotoAlbums.objects.filter(album_id = album.pk)

    data = {
        'title': album.title,
        'bgphoto': album.photo,
        'menu': menu,
        'photos': photos,
    }
    return render(request, 'main/album.html', data)

def gallery(request):
    albums = Album.objects.all()
    data = {
        'albums': albums,
        'menu': menu,
        'title': 'Gallery Albums'
    }
    return render(request, 'main/gallery-album.html', data)

def video(request):
    pass

def blog(request):
    pass

def contact(request):

    error_form = ''
    if request.method == 'POST':
        form = ContactForm(request.POST)
        data = {'form': form, 'menu': menu, 'title': 'Contact'}
        if form.is_valid():
            token = "2028468296:AAHXGxkKLclFHDEVBhU-a1QLKOIy3BZ01lM"
            url = "https://api.telegram.org/bot"
            channel_id = "257021138"
            url += token
            method = url + "/sendMessage"
            text = form.cleaned_data
            print(text)
            r = requests.post(method, data={
                "chat_id": channel_id,
                "text": f'''Имя: {text.get('name', 'Нет данных')}
Номер телефона: {text.get('phone')}
Email: {text.get('email')}
Работа: {text.get('subject')}
Сообщение: {text.get('message')}
'''
            })
            if r.status_code != 200:
                raise Http404
            else:
                return redirect('main:sentmessage')

        else:
            return render(request, 'main/contact.html', data)

    else:
        form = ContactForm()
        data = {'form': form, 'menu': menu, 'title': 'Contact'}
        return render(request, 'main/contact.html', data)

def sentmessage(request):

    return render(request, 'main/messagesent.html', {'menu': menu, 'title':'Messagesent'})


