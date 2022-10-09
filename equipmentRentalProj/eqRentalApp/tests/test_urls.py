from django.test import SimpleTestCase
from django.test import SimpleTestCase
from django.urls import reverse, resolve

from eqRentalApp.views import equipmnent_view, register_view, rent_view, your_rents_view

class TestUrls(SimpleTestCase):

    # Testing order_urls
    def test_order_urls_orders_add_is_resolved(self):
        url = reverse('equipment')
        self.assertEquals(resolve(url).func, equipment_view)

    def test_order_urls_myorders_is_resolved(self):
        url = reverse('register')
        self.assertEquals(resolve(url).func, register_view)

    def test_order_urls_user_order_is_resolved(self):
        url = reverse('rent', args=['1'])
        self.assertEquals(resolve(url).func, rent_view)

    def test_order_urls_pay_is_resolved(self):
        url = reverse('your-rents')
        self.assertEquals(resolve(url).func, your_rents_view)