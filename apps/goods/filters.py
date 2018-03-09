# -*- coding: utf-8 -*-
# @author ZhengZhong,Jiang
# @time 2017/11/16 17:09

import django_filters
from .models import Goods


class GoodsFilter(django_filters.rest_framework.FilterSet):
    price_min = django_filters.NumberFilter(name='shop_price', lookup_expr='gte')
    price_max = django_filters.NumberFilter(name='shop_price', lookup_expr='lte')
    name = django_filters.CharFilter(name="name", lookup_expr="icontains")

    class Meta:
        model = Goods
        fields = ['price_min', 'price_max', 'name']