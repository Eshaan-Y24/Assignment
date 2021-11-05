from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .models import Product, Category
from django.http import JsonResponse
import json

# class ProductList(APIView):

#     def get(self, request):
#         products = Product.objects.all()
#         serializer = ProductSerializer(products, many=True)
#         return HttpResponse(serializer.data)

#     def post(self):
#         pass

# Create your views here.


def products(request):
    data1 = list(Product.objects.values())
    data2 = list(Category.objects.values())
    categorylist = []

    for j in data2:
        categorylist.append(j['category_title'])

    for i in data1:
        index = i['category_id']-1
        i['category_id'] = categorylist[index]
    return JsonResponse(data1, safe=False)


def categories(request):
    data2 = list(Category.objects.values())
    categorylist = []

    for j in data2:
        categorylist.append(j['category_title'])

    return JsonResponse(data2, safe=False)
