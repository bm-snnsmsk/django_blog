from django.shortcuts import render ,HttpResponse, get_object_or_404,HttpResponseRedirect, redirect
from post.models import Post
from post.forms import PostForm


# Create your views here.

def index(r) :
    # return HttpResponse("index sayfasıu")
    # content = {
    #     'name' :'sinan şimşek'
    # }
    posts = Post.objects.all()
    return render(r,'post/index.html',{'posts':posts})

def detail(r, post_id) :
    post = get_object_or_404(Post, id= post_id)
    context = {'post':post}
    return render(r,'post/detail.html',context)

def delete(r, del_id) :
    del_post = get_object_or_404(Post, id= del_id)
    del_post.delete()
    return redirect("post:index")

def update(r,id) :
    post = get_object_or_404(Post, id= id)
    form = PostForm(r.POST or None, instance=post)
    if form.is_valid() :
        form.save()
        return HttpResponseRedirect(post.get_absolute_url())
    else :
        print("hata : validation")

    context = {
        'form':form
    }

    return render(r,'post/form.html',context)

def create(r) :
    
    
    # if r.method == "POST" :
    #     print(r.POST)

    ## DB'ye hkayıt ekleme     !!! tavsiye edilmiyor  111
    # title = r.POST.get('title')
    # content = r.POST.get('content')
    # Post.objects.create(title = title, content = content)

    ## tavsiye edilen yöntem  222 
    # if r.method == 'POST' :
    #     ## formadan gelen veiyi kaydet
    #     form = PostForm(r.POST)
    #     if form.is_valid() :
    #         result = form.save()
    #         return HttpResponseRedirect(result.get_absolute_url())
    #     else:
    #         print("bilgiler geçersiz")
    # else :
    #     ## frormu kullanıcıya göster
    #     form = PostForm()
    
    ## alternatif yöntem --- 333
    form = PostForm(r.POST or None)
    if form.is_valid() :
        result = form.save()
        return HttpResponseRedirect(result.get_absolute_url())
    else:
        print("bilgiler geçersiz")
    ############################################

    context = {
        'form':form
    }


    return render(r,'post/form.html',context)