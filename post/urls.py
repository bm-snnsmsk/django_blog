from django.urls import path
from . import views

app_name = "post" ## başka uygulamalrda detail olursa hata vereceğinden bu isimle de çağrılsa hata ortdan kalkacaktır

urlpatterns = [
    path('index/', views.index, name="index"),
    #path('detail/', views.detail, name="detail"),
    # path('<int:post_id>/', views.detail, name="detail"),
    path('create/', views.create, name="create"),

    path('<int:id>/', views.detail, name="detail"),  ## slug alanı
    path('<int:id>/update/', views.update, name="update"),
    path('<int:del_id>/delete/', views.delete, name="delete"),
]


