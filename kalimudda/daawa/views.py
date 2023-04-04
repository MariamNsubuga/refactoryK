from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Product, Sale
#these includes the filter models
from .filters import Product_filter
#including our model forms created in the forms.py
from .forms import AddForm, SaleForm

# Create your views here.

# def home(request):
#     return HttpResponse('Hello World') this will display helloworld in the broswer
#

def index(request):
    # return HttpResponse('Hello World')
    products = Product.objects.all().order_by('-id')
    products_filters = Product_filter(request.GET, queryset = products)
    products = products_filters.qs
    return render(request, 'products/index.html', {'products':products, 'product_filters':products_filters})


@login_required
def home(request):
    return render(request, 'products/aboutDrkali.html')


'''
@login_required decorators, it has to be excuted before the next function
'''
@login_required 
def product_detail(request, product_id):
    product = Product.objects.get(id = product_id)
    return render(request, "products/product_detail.html",{'product':product})

@login_required
def issue_item(request, pk):
    issued_item = Product.objects.get(id = pk)
    sales_form =  SaleForm(request.POST)
    if request.method == 'POST':

        #checks if the inputs is as its supposed to be
        if sales_form.is_valid():
            new_sale = sales_form.save(commit = False)
            new_sale.item = issued_item
            new_sale.unit_price = issued_item.unit_price
            new_sale.save()
            #to keep track of the stock remaining after the sales
            issued_quantity = int(request.POST['quantity'])
            issued_item.total_quantity -= issued_quantity
            issued_item.save()
            print(issued_item.item_name)
            print(request.POST['quantity'])
            print(issued_item.total_quantity) 

            return redirect('receipt')
        
    return render(request, 'products/issue_item.html',{'sales_form':sales_form})    
        
#this handles the receipt issuing
@login_required
def receipt(request):
    sales = Sale.objects.all().order_by('-id')
    return render (request, "products/receipt.html",{'sales':sales})

    

@login_required
def add_to_stock(request, pk):
    issued_item = Product.objects.get(id=pk)
    form = AddForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            add_quantity = int(request.POST['received_quantity']) #issuied_quantity
            issued_item.total_quantity += add_quantity
            issued_item.save()
            
            # to add to the remaining stock quantity has to reduce
            print(add_quantity)
            print(issued_item.total_quantity)
            return redirect('index')

    return render(request,'products/add_to_stock.html',{'form':form})


#this handles sales request 
#view is a function in django, method is a function in OOP
def all_sales(request):
    sales = Sale.objects.all()
    total = sum([items.amount_received for items in sales])
    change = sum([items.get_change() for items in sales])
    net = total - change
    return render(request,'products/all_sales.html',
                  {'sales':sales,
                   'total':total,
                   'change':change, 
                   'net':net,
                     })

     
