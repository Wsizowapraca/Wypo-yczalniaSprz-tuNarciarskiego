from email.policy import default
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MinValueValidator
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save

class User(AbstractUser):
    rented_eq = models.ForeignKey("Rent", on_delete=models.CASCADE, null=True, default=None)
    

class Equipment(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField(validators=[MinValueValidator(0, message="Nie można dać mniej niż 0!")])
    description = models.CharField(max_length=500)
    price = models.DecimalField(decimal_places=2, max_digits=7)
    image = models.ImageField()

    def __str__(self):
        return self.name

class Rent(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    rented_eq = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    rented_date = models.DateTimeField(auto_now_add=True)
    end_of_rent_date = models.DateTimeField(null=True, default=None, blank=True)
    # penalty = models.DecimalField(decimal_places=2, max_digits=7)
    phone = models.CharField(max_length=12)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return f"{self.rented_eq} rented by {self.client}"

def post_rent_created_signal(sender, instance, created, **kwargs):
    if created:
        rent = Rent.objects.get(id=instance.id)
        eqId = rent.rented_eq.id
        equipment = Equipment.objects.get(id=eqId)
        equipment_quantity = equipment.quantity
        equipment_quantity = equipment_quantity - 1
        Equipment.objects.filter(id=eqId).update(quantity=equipment_quantity)

post_save.connect(post_rent_created_signal, sender=Rent)