# cart/cart.py
from decimal import Decimal
from django.conf import settings

from products.models import Product


class Cart(object):

    def __init__(self, request):
        """
        Initialize the cart.
        """
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def __iter__(self):
        """
        Iterate on the cart's products and get products from the database.

        :return: Iterate on the cart's products and get products from the
                 database.
        :rtype: None
        """
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)

        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]['product'] = product

        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        """
        Count all items in the cart.

        :return: Count all items in the cart.
        :rtype: int
        """
        return sum(item['quantity'] for item in self.cart.values())

    def add_product(self, product, quantity=1, update_quantity=False):
        """
        Add a product to the cart or update its quantity.

        :param product: Current product.
        :type product: Product
        :param quantity: Number of product to add. (default= 1)
        :type quantity: int
        :param update_quantity: Is it a quantity update? (default= False)
        :type update_quantity: bool
        :return: Add a product in the cart or update its quantity.
        :rtype: None
        """
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0,
                                     'price': str(product.price)}
        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    def remove_product(self, product):
        """
        Remove a product from the cart.

        :param product: Current product.
        :type product: Product
        :return: Remove a product from the cart.
        :rtype: None
        """
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
        self.save()

    def get_total_price(self):
        """
        Calculate the total price of the cart.

        :return: Calculate the total price of the cart.
        :rtype: float
        """
        return sum(Decimal(item['price']) * item['quantity']
                   for item in self.cart.values())

    def save(self):
        """
        Mark the session as modified to ensure that the cart is saved.

        :return: Mark the session as modified to ensure that the cart is saved.
        :rtype: None
        """
        self.session.modified = True

    def clear_cart(self):
        """
        Clear the cart content.

        :return: Clear the cart content.
        :rtype: None
        """
        del self.session[settings.CART_SESSION_ID]
        self.save()
