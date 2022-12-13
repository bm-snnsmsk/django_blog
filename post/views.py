from django.shortcuts import render ,HttpResponse, get_object_or_404,HttpResponseRedirect, redirect, Http404
from post.models import Post
from post.forms import PostForm
from django.contrib import messages
from django.utils.text import slugify


# Create your views here.

def index(r) :
    # return HttpResponse("index sayfasıu")
    # content = {
    #     'name' :'sinan şimşek'
    # }
    posts = Post.objects.all()
    return render(r,'post/index.html',{'posts':posts})

def detail(r, post_id) :
    post = get_object_or_404(Post, id= post_id) ## id yerine slug kullanılırsa id ile değiştirlmeli
    context = {'post':post}
    return render(r,'post/detail.html',context)

def delete(r, del_id) :
    if not r.user.is_authenticated(): ## giriş yapılmadıysa silme yapamaz
        return Http404()
    del_post = get_object_or_404(Post, id= del_id)## id yerine slug kullanılırsa id ile değiştirlmeli
    del_post.delete()
    return redirect("post:index")

def update(r,id) :
    if not r.user.is_authenticated(): ## giriş yapılmadıysa düzenleme yapamaz
        return Http404()

    post = get_object_or_404(Post, id= id)## id yerine slug kullanılırsa id ile değiştirlmeli
    form = PostForm(r.POST or None, r.FILES or None, instance=post)
    if form.is_valid() :

        #form.save() ## postu save 'e kaydet

        ## 2. yöntem için yoruöma alındı START
        # form.save(commit=False) ## postu save 'e kaydetmez ama nesneyi geri döndürür
        # # post.slug = slugify(post.title) ## ı harflerini siler
        # post.slug = slugify(post.title.replace("ı","i"))
        ## 2. yöntem için yoruöma alındı  END

        form.save() ## postu save 'e kaydet
        messages.success(r,"işlem başarılı")
        return HttpResponseRedirect(post.get_absolute_url())
    else :
        print("hata : validation")

    context = {
        'form':form
    }

    return render(r,'post/form.html',context)

def create(request) :
    if not request.user.is_authenticated:
        return Http404()
    
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
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid() :
        result = form.save()
        messages.success(request,"işlem başarılı")
        return redirect('post:index')
    else:
        print("bilgiler geçersiz")
    ############################################
    context = {
        'form':form
    }
    return render(request,'post/form.html',context)