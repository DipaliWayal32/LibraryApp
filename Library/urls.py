# from django.conf.urls import re_path 
from django.urls import re_path

from Library import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    # path('admin/',views.LibraryApi),
    # path('api/',views.LibraryApi),

    re_path(r'^Library$',views.LibraryApi),
    re_path(r'^Library/([0-9]+)$',views.LibraryApi),

    re_path(r'^Library/savefile',views.SaveFile)
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
