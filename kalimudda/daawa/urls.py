from django.urls import  path
from daawa import views
from django.contrib.auth import views as auth_views #this borrows the admin login and logout function of django

urlpatterns = [
    path('index/', views.index, name = "index"),
    path('', auth_views.LoginView.as_view(template_name = 'products/login.html'), name = "login"),
    path('home/', views.index, name = "home"),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'products/logout.html'), name = "logout"),
#    lists all products with the buy button
    path('index/<int:product_id>',views.product_detail, name = "product_detail"),
     #this route is for buying item (buy item button)
    path('issue_item/<str:pk>',views.issue_item, name = 'issue_item'),   
    path('add_to_stock/<str:pk>',views.add_to_stock, name = 'add_to_stock'), 
    #this handles the receipt after successful sales
    path('receipt/',views.receipt, name = 'receipt'),#handle a reciept after a successful sale
    #this handles the sales 
    path('all_sales/',views.all_sales, name = 'all_sales')
]