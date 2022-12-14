from app.models import Product
from app.serializers import ProductSerializer
from rest_framework import generics, filters


class ProductList(generics.ListCreateAPIView):
    search_fields = ['name', 'article']
    filter_backends = (filters.SearchFilter,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
