from django.shortcuts import render

from .serializers import GoodsSerializer, CategorySerializer
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import filters
from rest_framework import mixins

from django_filters.rest_framework import DjangoFilterBackend
from .models import Goods, GoodsCategory

from .filters import GoodsFilter

# Create your views here.


# class GoodsListView(APIView):
#     def get(self, request, format=None):
#         goods = Goods.objects.all()[:10]
#         goods_serializers = GoodsSerializer(goods, many=True)
#         return Response(goods_serializers.data)


class GoodsPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = 'p'
    max_page_size = 100


# class GoodsListView(ListAPIView):
#     queryset = Goods.objects.all()
#     serializer_class = GoodsSerializer
#     pagination_class = GoodsPagination

class GoodsListView(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    商品列表页，分页，搜索，过滤，排序
    """
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    pagination_class = GoodsPagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    # filter_fields = ('name', 'shop_price')
    filter_class = GoodsFilter
    search_fields = ("shop_price", "name")
    ordering_fields = ('sold_num', 'fav_num', 'add_time')


class CategoryViewset(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    List :
        商品分类列表数据
    """
    queryset = GoodsCategory.objects.filter(category_type=1)
    serializer_class = CategorySerializer