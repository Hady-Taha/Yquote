from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views
urlpatterns = [
    path('register/',views.register,name='register'),
    path('login/',views.vlogin,name='login'),
    path('logout/',views.vlogout,name='logout'),
    path('profile/<int:id>',views.profile,name='profile'),
    path('updateprofile/<int:id>',views.vupdateprofile,name='updateprofile')
]
urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)