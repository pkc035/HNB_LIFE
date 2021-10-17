from django.db.models import Q
from django.http import HttpResponse
from rest_framework          import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from .serializers import ShopSerializer
from .models      import Shop

class ShopViewSet(ModelViewSet):
    queryset         = Shop.objects.all()
    serializer_class = ShopSerializer
    
    def get_queryset(self):
        qs     = super().get_queryset()
        lat    = float(self.request.query_params.get('lat',0))
        lon    = float(self.request.query_params.get('lon',0))
        search = self.request.query_params.get('search',None)
        
        # 특정 키워드가 포함된 데이터 필터링
        if search:
            qs = qs.filter(Q(name__icontains=search)|Q(tags__icontains=search))
        
        # lat, lon 위치 데이터를 기준으로 가까운거리로 정렬하기 위해 sorted 함수를 사용하여
        # 저장된 shop의 lat,lon과 query_param으로 받은 lat, lon을 가지고 제곱 계산하여 거리 계산
        if (lat > 0) & (lon > 0):
            qs = sorted(qs, key=lambda shop : pow(shop.lat-lat,2)+pow(shop.lon-lon,2))

        return qs