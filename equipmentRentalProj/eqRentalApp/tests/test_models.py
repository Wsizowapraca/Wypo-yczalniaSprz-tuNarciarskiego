from django.test import TestCase
from base.models import Equipment, Rent
from django.contrib.auth.models import User

class TestModels(TestCase):

    def setUp(self):

        self.user = User.objects.create(
            username = "username",
            password = "password"
        )

        self.eq1 = Equipment.objects.create(

            name = "myequipment",
            description = "my_description",
            quantity = 10,
            price = 12.4,
          image = "image.png"
        )

        self.rent1 = Rent.objects.create(
            client = self.user,
            rented_eq = self.eq1,
            rented_date = "2022/12/12 12:12:12",
            end_of_rent_date = "2022/12/12 13:13:13",
            phone = 414241414,
            email = "testemail@email.com"

        )


    def test_Equipment(self):
        self.assertEquals(self.product1.name, "myequipment")
        self.assertEquals(self.product1.description, "my_description")
        self.assertEquals(self.product1.quantity, 10)
        self.assertEquals(self.product1.image, "image.png")


    def test_Rent(self):
        self.assertEquals(self.order1.client, self.user)
        self.assertEquals(self.order1.rented_eq, self.eq1)
        self.assertEquals(self.order1.rented_date, "2022/12/12 12:12:12")
        self.assertEquals(self.order1.end_of_rent_date, "2022/12/12 13:13:13")
        self.assertEquals(self.order1.tphone, 414241414)
        self.assertEquals(self.order1.email, "testemail@email.com")