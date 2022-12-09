from django.db import models
from django.urls import reverse  ## hata verdi

# Create your models here.

class Post(models.Model) :
    title = models.CharField(max_length=100, verbose_name="Başlık")
    content = models.TextField(verbose_name="İçerik")
    publishing_date = models.DateTimeField(verbose_name="Yayınlanma Tarihi",auto_now_add=True) ## şimdiki tarihi otomatik olarak ata

    def __str__(self) :
        return self.title

    def get_absolute_url(self) :
        ## return reverse('post:detail', kwargs={'id' : self.id} ) ## en dinamik olanı  post:detail = app_name = "post"
        return "/post/{}".format(self.id) ## parantez içine her nesnenin id'si çağrılacak 
