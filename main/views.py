from django.shortcuts import render

def dev(request):
    return render(request, 'main/dev.html')

def index(request):
    return render(request, 'main/index.html')

def contacts(request):
    return render(request, 'main/contacts.html')

def gallery(request):
    return render(request, 'main/gallery.html')

def handler404(request, exception):
    return render(request, 'main/404.html', status=404)
    
def page_404(request):
    return render(request, 'main/404.html')