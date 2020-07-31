from rest_framework import serializers
from .models import Goods, GoodsCategory


class CategorySerializer3(serializers.ModelSerializer):
    class Meta:
        model = GoodsCategory
        fields = '__all__'


class CategorySerializer2(serializers.ModelSerializer):
    # 通过二级分类目录获取到三级分类
    sub_category = CategorySerializer3(many=True)

    class Meta:
        model = GoodsCategory
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    # 通过一级分类目录获取到二级分类，由于一级分类下有多个二级分类，需要设置many= True
    sub_category = CategorySerializer2(many=True)

    class Meta:
        model = GoodsCategory
        fields = '__all__'


class GoodsSerializer(serializers.ModelSerializer):
    # 自定义字段覆盖原有的字段，实例化
    category = CategorySerializer()

    class Meta:
        model = Goods
        # fields = ('id', 'name', 'category', 'shop_price', 'goods_front_image')
        fields = '__all__'

    def create(self, validated_data):
        """
        给定经过验证的数据，创建并返回一个新的“Goods”实例。
        """
        return Goods.objects.create(**validated_data)