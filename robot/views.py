from django.shortcuts import render
from vanilla import TemplateView
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from rest_framework import authentication, permissions, viewsets
from rest_framework import viewsets
from robot.serializers import RobotSerializer
from rest_framework.authtoken.models import Token
from robot.models import Robot


class LoginRequiredView(object):
    @method_decorator(staff_member_required())
    def dispatch(self, *args, **kwargs):
        return super(LoginRequiredView, self).dispatch(*args, **kwargs)


class DefaultsMixin(object):
    authentication_classes = (
        authentication.BasicAuthentication,
        authentication.TokenAuthentication,
    )

    permission_classes = (
        permissions.IsAuthenticated,
    )

    authentication_classes = (
        authentication.TokenAuthentication,
    )


class RobotViewSet(DefaultsMixin, viewsets.ModelViewSet):
    queryset = Robot.objects.all()
    serializer_class = RobotSerializer


class RobotControllerView(LoginRequiredView, TemplateView):
    template_name = 'controller.html'

    def get_context_data(self, **kwargs):
        contex = super(RobotControllerView, self).get_context_data(**kwargs)
        contex['token'] = Token.objects.get(user=self.request.user)
        contex['user'] = self.request.user.pk
        return contex


class RobotUserIndex(LoginRequiredView, TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        contex = super(RobotUserIndex, self).get_context_data(**kwargs)
        contex['objects_list'] = Robot.objects.filter(user=self.request.user)
        return contex
