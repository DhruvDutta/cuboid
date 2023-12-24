
from django.conf.urls import handler404
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
    path('', include('main.urls')),
    path('api/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/token/', obtain_auth_token, name='api_token_auth'),
    path('admin/', admin.site.urls),
]
handler404 = 'main.views.error_404_handler'
