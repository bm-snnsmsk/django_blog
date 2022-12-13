from django.db import models
from django.urls import reverse  ## hata verdi
from django.utils.text import slugify

# Create your models here.

class Post(models.Model) :
    #user = models.ForeignKey('auth.User', verbose_name="yazar", related_bane= "posts") 
    title = models.CharField(max_length=120, verbose_name="Başlık")
    content = models.TextField(verbose_name="İçerik")
    publishing_date = models.DateTimeField(verbose_name="Yayınlanma Tarihi",auto_now_add=True) ## şimdiki tarihi otomatik olarak ata
    image = models.FileField(null=True, blank=True) ## zorunlu değil boş geçilebilir demek
    ## slug = models.SlugField(unique=True, editable=False, max_length=130) ## slug ,  editable=False = panelde görünmez sadece programatik olarak değer atanır

    def __str__(self) :
        return self.title

    def get_absolute_url(self) :
        ## return reverse('post:detail', kwargs={'id' : self.id} ) ## en dinamik olanı  post:detail = app_name = "post" ## slug kullanılırsa id yerine kullanılmalı
        return "/post/{}".format(self.id) ## parantez içine her nesnenin id'si çağrılacak 

    def get_create_url(self) :
        return reverse('post:create')

    def get_update_url(self) :
        return reverse('post:update', kwargs={'id' : self.id} ) ## slug kullanılırsa id yerine kullanılmalı

    def get_delete_url(self) :
        return reverse('post:delete', kwargs={'id' : self.id} )## slug kullanılırsa id yerine kullanılmalı


    ## sluglar aynı olursa diye önlem amaçlı fonksiyon
    # def get_unique_slug(self) :
    #     slug = slugify(self.title.replace("ı","i"))
    #     unique_slug = slug 
    #     counter = 1
    #     while Post.objects.filter(slug=unique_slug).exists() :
    #         unique_slug = "{} - {}".format(slug, counter)
    #         counter += 1
    #     return unique_slug


    ## slug 'ı tanımlamanın 2. yolu 
    ## save() 'i override etme
    # def save(self, *args, **kwargs) :
    #     ## slug alanı 1 kere üretilmek için
    #     # if not self.slug :
    #     #     self.slug = self.get_unique_slug()
    #     # return super(Post, self).save(*args, **kwargs)

       
    #     self.slug = self.get_unique_slug()
    #     return super(Post, self).save(*args, **kwargs)


    class Meta :
        ordering = ['-publishing_date', 'id'] ## -publishing_date yeniden eskiğye
