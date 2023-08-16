from django.urls import path
from .views import FoodTypeListCreateAPIView, FoodItemListCreateAPIView, CartAddAPIView, OrderCreateAPIView, \
    UserOrderListAPIView, FoodItemDetailAPIView

urlpatterns =[
    path('food-types/',FoodTypeListCreateAPIView.as_view(),name='food_types_list_create'),
    path('food-items/',FoodItemListCreateAPIView.as_view(),name='food-item-list-create'),
    path('food-items/<int:pk>/', FoodItemDetailAPIView.as_view(), name='food-item-detail'),
    path('add-to-cart/', CartAddAPIView.as_view(), name='add_to_cart'),
    path('place-order/', OrderCreateAPIView.as_view(), name='place_order'),
    path('my-orders/', UserOrderListAPIView.as_view(), name='my_orders'),
]