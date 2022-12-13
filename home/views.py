from django.shortcuts import render, HttpResponse

# Create your views here.
def home_view(req) :
    # return HttpResponse("home sayfası  django")
    if req.user.is_authenticated :
        content = {'name' :'sinan şimşek',}
    else :
        content = {'name' :' Misafir',}
    return render(req,'home/anasayfa.html', content)