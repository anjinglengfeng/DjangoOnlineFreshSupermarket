from django_filters import rest_framework as filters
from .models import Goods


class GoodsFilter(filters.FilterSet):
    """
    商品的过滤类
    """
    name = filters.CharFilter(field_name='name', lookup_expr='contains')  # 包含关系，模糊匹配
    goods_desc = filters.CharFilter(field_name='name', lookup_expr='contains')
    min_price = filters.NumberFilter(field_name="shop_price", lookup_expr='gte')  # 自定义字段
    max_price = filters.NumberFilter(field_name="shop_price", lookup_expr='lte')

    class Meta:
        model = Goods
        fields = ['name', 'goods_desc', 'min_price', 'max_price']