#form is an interface where a user creates data
from django.forms import ModelForm 
#accessing our models sothat we can link them to our forms
from .models import * 

class AddForm(ModelForm):
    #meta helps us access a model and manipulate it 
    class Meta:
        model = Product
        fields = ['received_quantity']#update already existing form
#we are modeling a form basing on our model for us to record a given product sale
class SaleForm(ModelForm):
    class Meta:
        model = Sale
        fields = ['quantity','amount_received','issued_to']