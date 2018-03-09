# -*- coding: utf-8 -*-
# @author ZhengZhong,Jiang
# @time 2017/11/10 14:18

from rest_framework import serializers

from .models import Goods, GoodsCategory


# class GoodsSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=50)
#     click_num = serializers.IntegerField(default=0)
#     goods_front_image = serializers.ImageField()

class CategorySerializer3(serializers.ModelSerializer):
    class Meta:
        model = GoodsCategory
        fields = "__all__"


class CategorySerializer2(serializers.ModelSerializer):
    sub_cat = CategorySerializer3(many=True)

    class Meta:
        model = GoodsCategory
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    sub_cat = CategorySerializer2(many=True)

    class Meta:
        model = GoodsCategory
        fields = "__all__"


class GoodsSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    
    class Meta:
        model = Goods
        # fields = ('goods_sn', 'name', 'click_num', 'market_price', 'add_time')
        fields = ('__all__')

