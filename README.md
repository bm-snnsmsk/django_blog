// virtual 1. adım
pip install virtualenv

// virtual 2. adım // kurulacak klasör
virtualenv venv_folder_name

// virtual 3.  adım // aktivasyon için
source venv_folder_name/Scripts/activate


// deaktivasyon için
venv_folder_name\Scripts\deactivate


// install işlemi
pip install Django

// mysql için
pip install mysqlclient

// django >
django-admin startproject project_name .  // proje oluşturma . = bu dizine kur(ekstra bir klasor açmaya gerek kalmaz)

// django > project_name
python manage.py help    // django ile çalıştırılabilecek komutlar 
django-admin help        // django ile çalıştırılabilecek komutlar 

// django > project_name
python manage.py startapp app_name  // uygulama oluşturma

python manage.py runserver  // dosyayı çalıştırma komutu


python manage.py makemigrations // yeni oluşturulan tablo için migrate oluşturmak 

python manage.py migrate // migrate etmek // tabloyu database eklemek

// modelin sql görünümü
python manage.py sqlmigrate post 0001// migrate etmek // model_name 0001_initial.py(4 rakam) 

// admin 
python manage.py createsuperuser   

//
python manage.py shell


