from django.shortcuts import render
from rest_framework import generics, permissions, status
from rest_framework.response import Response

from .models import FoodType, FoodItem, UserOrder, Cart
from .serializer import FoodTypeSerializer, FoodItemSerializer, CartSerializer, UserOrderSerializer


# Create your views here.

class FoodTypeListCreateAPIView(generics.ListCreateAPIView):
    queryset = FoodType.objects.all()
    serializer_class = FoodTypeSerializer
    permission_classes = (permissions.AllowAny,)

class FoodItemListCreateAPIView(generics.ListCreateAPIView):
    queryset = FoodItem.objects.all()
    serializer_class = FoodItemSerializer
    permission_classes = (permissions.IsAdminUser,)

class FoodItemDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = FoodItem.objects.all()
    serializer_class = FoodItemSerializer
    permission_classes = (permissions.IsAdminUser,)


class CartAddAPIView(generics.CreateAPIView):
    serializer_class = CartSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        cart = serializer.save()
        return Response(CartSerializer(cart).data, status=status.HTTP_201_CREATED)

class UserOrderListAPIView(generics.ListAPIView):
    serializer_class = UserOrderSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return UserOrder.objects.filter(user=self.request.user)
class OrderCreateAPIView(generics.CreateAPIView):
    queryset = UserOrder.objects.all()
    serializer_class = UserOrderSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        user_cart = Cart.objects.filter(user=self.request.user)
        items = [cart.food_item for cart in user_cart]
        serializer.save(user=self.request.user, items=items)
        user_cart.delete()
