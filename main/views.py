from django.shortcuts import render

def index(request):
    return render(request, 'main/index.html')

def handler404(request, exception):
    return render(request, 'main/404.html', status=404)
    
def page_404(request):
    return render(request, 'main/404.html')