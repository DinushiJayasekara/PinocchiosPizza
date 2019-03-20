from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Menu_Regular_Pizza(models.Model):
    name = models.CharField(max_length=64)
    small = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    large = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    idname = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.id} {self.name}: Small. . . . . . . . . . . . . . . . . . . .${self.small}: Large. . . . . . . . . . . . . . . . . . . .${self.large}"

class Menu_Sicilian_Pizza(models.Model):
    name = models.CharField(max_length=64)
    small = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    large = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    idname = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.id} {self.name}: Small. . . . . . . . . . . . . . . . . . . .${self.small}: Large. . . . . . . . . . . . . . . . . . . .${self.large}"

class Menu_Topping(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.id} {self.name}"

class Menu_Sub(models.Model):
    name = models.CharField(max_length=64)
    small = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    large = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    idname = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.id} {self.name}: Small. . . . . . . . . . . . . . . . . . . .${self.small}: Large. . . . . . . . . . . . . . . . . . . .${self.large}"

class Menu_Pasta(models.Model):
    name = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    idname = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.id} {self.name}. . . . . . . . . . . . . . . . . . . .${self.price}"

class Menu_Salad(models.Model):
    name = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    idname = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.id} {self.name}. . . . . . . . . . . . . . . . . . . .${self.price}"

class Menu_Dinner_Platter(models.Model):
    name = models.CharField(max_length=64)
    small = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    large = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    idname = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.id} {self.name}: Small. . . . . . . . . . . . . . . . . . . .${self.small} Large. . . . . . . . . . . . . . . . . . . .${self.large}"

class Menu_Sub_Extra(models.Model):
    name = models.CharField(max_length=64)
    small = models.DecimalField(max_digits=5, decimal_places=2)
    large = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.id} {self.name}: Small. . . . . . . . . . . . . . . . . . . .${self.small} Large. . . . . . . . . . . . . . . . . . . .${self.large}"

class Order(models.Model):
    username = models.CharField(max_length=64)
    size = models.CharField(max_length=64)
    quantity = models.IntegerField(null=True, blank = True)
    type = models.CharField(max_length=64,null=True, blank = True)
    extra = models.CharField(max_length=64,null=True, blank = True)
    smallprice = models.CharField(max_length=64,null=True, blank = True)
    largeprice = models.CharField(max_length=64,null=True, blank = True)
    price = models.CharField(max_length=64,null=True, blank = True)
    
    def __str__(self):
        return f"{self.id} User:{self.username} Size:{self.size} Quantity:{self.quantity} Type:{self.type} Extras:{self.extra}"

class All_Order(models.Model):
    username = models.CharField(max_length=64)
    size = models.CharField(max_length=64)
    quantity = models.IntegerField(null=True, blank = True)
    type = models.CharField(max_length=64,null=True, blank = True)
    extra = models.CharField(max_length=64,null=True, blank = True)
    smallprice = models.CharField(max_length=64,null=True, blank = True)
    largeprice = models.CharField(max_length=64,null=True, blank = True)
    price = models.CharField(max_length=64,null=True, blank = True)

    def __str__(self):
        return f"{self.id} User:{self.username} Size:{self.size} Quantity:{self.quantity} Type:{self.type} Extras:{self.extra}"
