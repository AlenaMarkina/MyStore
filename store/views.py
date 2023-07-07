from django.shortcuts import render
from django.views import View
from django.db.models import OuterRef, Subquery, F, ExpressionWrapper, DecimalField, Case, When
from django.utils import timezone
from .models import Product, Wishlist


class ProductSingleView(View):
    def get(self, request, id):
        data = Product.objects.get(id=id)
        return render(request,
                      'store/product-single.html',
                      context={'name': data.name,
                               'description': data.description,
                               'price': data.price,
                               'rating': 5.0,
                               'url': data.image.url,
                               })


class CartView(View):
    def get(self, requests):
        return render(requests, 'store/cart.html')


class ShopView(View):
    def get(self, request):
        # Создание запроса на получение всех действующих не нулевых скидок
        discount_value = Case(When(discount__value__gte=0,
                                   discount__date_begin__lte=timezone.now(),
                                   discount__date_end__gte=timezone.now(),
                                   then=F('discount__value')),
                              default=0,
                              output_field=DecimalField(max_digits=10, decimal_places=2)
                              )

        # Создание запроса на расчет цены со скидкой
        price_with_discount = ExpressionWrapper(
            F('price') * (100.0 - F('discount_value')) / 100.0,
            output_field=DecimalField(max_digits=10, decimal_places=2)
        )

        products = Product.objects.annotate(
            discount_value=discount_value,
            # Другой способ через запрос в другую таблицу, однако
            # без фильтрации по времени действия скидки
            # discount_value=Subquery(
            #     Discount.objects.filter(product_id=OuterRef('id')).values(
            #         'value')
            # ),
            price_before=F('price'),
            price_after=price_with_discount
        ).values('id', 'name', 'image', 'price_before', 'price_after',
                 'discount_value')
        return render(request, 'store/shop.html', {"data": products})


class WishlistView(View):
    def get(self, request):
        data = Wishlist.objects.select_related('product')  # data=<QuerySet [<Wishlist: Tomatoes>]>

        print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        print(f'data = {data},\ndata[0] = {data[0]},\ndata[0].product = {data[0].product}\ndata[0].product.price = {data[0].product.price},\n{data[0].product.__dict__}')
        print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n')

        for product in data:
            print(product)
            # print(product[0].product.description, 11111111111111)

        return render(request, 'store/wishlist.html', context={'data': data})
