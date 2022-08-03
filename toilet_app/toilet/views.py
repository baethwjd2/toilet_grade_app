from http.client import HTTPResponse
from .models import Toilet
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from haversine import haversine, Unit
from .serializers import ToiletSerializer
from django.db.models import Q
from django.shortcuts import render

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 1000

class ToiletViewSet(ModelViewSet):

    toilets = Toilet.objects.all()
    queryset = toilets
    serializer_class = ToiletSerializer
    pagination_class = StandardResultsSetPagination

    @action(detail=False)
    def search(self, request):

        # 유저 정보 GET Request
        lat = request.GET.get("lat", None)
        lon = request.GET.get("lon", None)
        gen = request.GET.get("gen", None)
        is_disabled = request.GET.get("is_disabled", None)
        is_child = request.GET.get("is_child", None)
        max_distance = request.GET.get("max_distance", None)

        # 사용자 위치로부터 화장실 거리 계산
        loc_user = (lat, lon)

        for toilet in self.toilets:
            try:
                loc_toilet = (toilet.latitude, toilet.longitude)
                toilet.distance = haversine(loc_user, loc_toilet, unit='m')
            except:
                pass

        # 필터링
        q = Q()

        if max_distance is not None:
            q.add(Q(distance__lte=max_distance), q.AND)

        if gen is not None:
            if gen==0:
                q.add(Q(manToiletNum__gte=0), q.AND)
                q.add(Q(isBisexual=True), q.OR)
            if gen==1:
                q.add(Q(womanToiletNum__gte=0), q.AND)
                q.add(Q(isBisexual=True), q.OR)

        if is_disabled is not None and is_disabled:
            if gen==0:
                q.add(Q(manDisabledToiletNum__gte=0), q.AND)
            if gen==1:
                q.add(Q(womanDisabledToiletNum__gte=0), q.AND)

        if is_child is not None and is_child:
            q.add(Q(childUrinalNum__gte=0), q.AND)

        paginator = self.paginator

        try:
            result = Toilet.objects.filter(q)
        except ValueError:
            result = Toilet.objects.all()
        results = paginator.paginate_queryset(self.toilets, request)
        serializer = ToiletSerializer(results, many=True)

        return paginator.get_paginated_response(serializer.data)


            

        
        



