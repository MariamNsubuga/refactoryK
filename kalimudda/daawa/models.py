from django.db import models

# Create your models here.

#models means decription of the space on the database where we store things
#models are python classes


class Category(models.Model):
    name = models.CharField(max_length = 50, null = True, blank = True)
# This method gives a human readable name for the Object of the class which is our Category    
    def __str__(self):
        return self.name
    
#creating rowsand columns
class Product(models.Model):
# Here we are connecting product model to Category model 
# A foreign key is a column in one table that is being referenced in another table   
    category_name = models.ForeignKey(Category,on_delete=models.CASCADE, null=True, blank=True)

    item_name = models.CharField(max_length = 50, null = True, blank = True)
    total_quantity = models.IntegerField(default = 0, null = True, blank = True)
    issuied_quantity = models.IntegerField(default = 0, null = True, blank = True)
    received_quantity = models.IntegerField(default = 0, null = True, blank = True)
    unit_price = models.IntegerField(default = 0, null = True, blank = True)
    manufacturer = models.CharField(max_length = 50, null = True, blank = True)
    brand = models.CharField(max_length = 50, null = True, blank = True)

    def __str__(self):#this ends the model always
        return self.item_name

class Sale(models.Model):
    #the item name,purcharcers name, purchase,quantity, vat(total*0.18),date received, person who sold
    item = models.ForeignKey(Product, on_delete= models.CASCADE)
    quantity = models.IntegerField(default = 0, null = False, blank = True)
    amount_received = models.IntegerField(default = 0, null = False, blank = True)
    issued_to = models.CharField(max_length = 50, null = True, blank = True)
    unit_price = models.IntegerField(default = 0, null = True, blank = True)
    sold_at = models.DateTimeField(auto_now_add= True)
    def get_total(self):
        total = self.quantity * self.item.unit_price
        return int(total)  #converting to interger
    def get_change(self):
        change = self.get_total() - self.amount_received
        return abs(int(change))
    def get_vat(self):
        pass
    
    def __str__(self):
        return self.item.item_name

