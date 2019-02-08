from django.http import HttpResponse, HttpResponseNotFound
import datetime

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><head><title>Main Page</title></head><body><h1>It is now %s</h1><p>This is simple view showing current date.</p></body></html>" % now
    return HttpResponse(html)

def my_view(request):
    foo = ''
    if foo:
        return HttpResponseNotFound('<h1>Page not found</h1>')
    else:
        return HttpResponse('<h1>Page was found</h1>')
