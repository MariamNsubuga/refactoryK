from django.contrib import admin
from .models import *

# Register your models here.
#Here i am creating a models to appear on the admin dashboard 
admin.site.register(Category)
admin.site.register(Product)
#admin can also register a sale
admin.site.register(Sale)

