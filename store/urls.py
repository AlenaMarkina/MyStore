from django.urls import path
from rest_framework import routers
from .views import ProductSingleView, ShopView, WishlistView, CartViewSet, CartView,\
    delete_from_wishlist, add_to_wishlist

router = routers.DefaultRouter()
router.register(r'cart', CartViewSet)

app_name = 'store'

urlpatterns = [
    path('', ShopView.as_view(), name='shop'),
    path('cart/', CartView.as_view(), name='cart'),
    path('product/<int:id>/', ProductSingleView.as_view(), name='product'),
    path('wishlist/', WishlistView.as_view(), name='wishlist'),
    path('wishlist/del/<int:id>', delete_from_wishlist, name='delete'),
    path('wishlist/add/<int:id>', add_to_wishlist, name='add')
]
