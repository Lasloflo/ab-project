from django.shortcuts import render

# Create your views here.

menu = {
    'Home': 'main:home',
    'About': 'main:about',
    'Services': 'main:services',
    'Gallery': 'main:gallery',
    'Video': 'main:video',
    'Blog': 'main:blog',
    'Contact': 'main:contact',
}


def index(request):
    context = {
        'menu': menu,
    }

    return render(request, 'main/index.html', context)
