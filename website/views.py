from django.shortcuts import render




def home(request):
    return render(request, 'website/home.html')

def gallery(request):
    return render(request, 'website/gallery.html')

def contact(request):
    return render(request, 'website/contact.html')

def about(request):
    return render(request, 'website/about.html')

def promo(request):
    return render(request, 'website/promo.html')

def stock(request):
    return render(request, 'website/stock.html')

def events(request):
    return render(request, 'website/events.html')