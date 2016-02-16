from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.authtoken.views import obtain_auth_token
from robot.urls import router

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
    url(r'^api/token/', obtain_auth_token, name='api-token'),
    url(r'^api/robot/', include(router.urls)),
    url(r'^robot/', include('robot.urls')),
]
