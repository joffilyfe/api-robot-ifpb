from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from robot import views

router = DefaultRouter()
router.register(r'command', views.RobotViewSet)


urlpatterns = [
    url(r'^controller/(?P<pk>[0-9]+)/$',
        views.RobotControllerView.as_view(), name="robot_controller"),
]
