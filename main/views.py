from django.http import HttpResponse

def homePageView(request):
    html = "<html style='background-color: black; color: white; height: 100%; display: flex; align-items: center; justify-content: center;'><body><h1>CARNEBAR</h1></body></html>"
    return HttpResponse(html)
