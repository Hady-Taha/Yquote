from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views
urlpatterns = [
    path('',views.indexWeb,name='website'),
    path('home/', views.home , name='home'),
    path('delete/<int:id>', views.vdelete , name='delete'),
    #path('detail/', views.detail , name='detail'),
    
]
urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)