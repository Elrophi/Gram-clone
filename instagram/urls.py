from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views
from .views import Index


urlpatterns=[
    path('', Index.as_view(), name='index' ),
    path('accounts/', include('allauth.urls')),
    
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
