import datetime
from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from django.utils.translation import gettext_lazy as _

from directory.models import Site, SiteLog, SiteType, Direction
from directory.serailizers import SiteSerializer, SiteTypeSerializer, DirectionSerializer, SiteLogMainSerailizer, SiteLogSerailizer, SiteLogGetSerailizer
# Create your views here.


class DirectionView(generics.ListAPIView):
    queryset = Direction.objects.all()
    serializer_class = DirectionSerializer


class SiteListView(generics.ListAPIView):
    queryset = Site.objects.all().prefetch_related('logs', 'types')
    serializer_class = SiteSerializer


class SiteLogRetrieveAPIView(generics.GenericAPIView):
    queryset = SiteLog.objects.all()
    serializer_class = SiteLogMainSerailizer

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        instance.update_visitor_count()
        return Response(serializer.data)


class SiteLogCreateView(generics.GenericAPIView):
    serializer_class = SiteLogMainSerailizer
    queryset = SiteLog.objects.all()

    def post(self, request, *args, **kwargs):
        data = request.data
        is_log = SiteLog.is_avaliable(
            site=data['site'], day=datetime.datetime.now().date())
        if is_log:
            return Response({
                'message': _('Already Added')
            },
                status=status.HTTP_400_BAD_REQUEST)
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class SiteLogRetrievView(generics.RetrieveAPIView):
    queryset = Site.objects.all()
    serializer_class = SiteLogSerailizer


class SiteLogView(generics.ListAPIView):
    queryset = SiteLog.objects.all().select_related(
        'site').prefetch_related('site__types')
    serializer_class = SiteLogGetSerailizer
