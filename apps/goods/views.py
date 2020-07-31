from django_filters.rest_framework import DjangoFilterBackend
from .models import Goods, GoodsCategory
from .serializers import GoodsSerializer, CategorySerializer
from rest_framework import viewsets, filters
from rest_framework import mixins
from rest_framework.pagination import PageNumberPagination
from .filters import GoodsFilter


class GoodsPagination(PageNumberPagination):
    page_size = 3  # 默认每一页个数
    page_size_query_param = 'page_size'
    page_query_param = 'p'  # 参数?p=xx
    max_page_size = 36  # 最大指定每页个数


class GoodsListView(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    显示所有的商品列表
    """
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    pagination_class = GoodsPagination


class GoodsListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    显示所有的商品列表
    """
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    pagination_class = GoodsPagination
    # 将过滤器后端添加到单个视图或视图集
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,)
    filterset_class = GoodsFilter
    # 搜索字段
    search_fields = ('name', 'goods_desc', 'category__name')
    ordering_fields = ('click_num', 'sold_num', 'shop_price')  # 排序

    def get_queryset(self):
        queryset = self.queryset
        # 传递价格区间的参数
        price_min = self.request.query_params.get('price_min')
        if price_min:
            queryset = queryset.filter(shop_price__gte=price_min)
        return queryset


class CategoryViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    list: 商品分类列表
    """
    # queryset = GoodsCategory.objects.all()
    queryset = GoodsCategory.objects.filter(category_type=1)
    serializer_class = CategorySerializer
