
from django.contrib import admin
from django.urls import path
from django.urls import include, re_path
from biashara import views

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('', include('biashara.urls'))
]
