import json
from django.http import JsonResponse
from django.shortcuts import render
from .models import *
import datetime
from .utils import cookieCart , cartData, guestOrder
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth import authenticate,login

def store(request):
    data = cartData(request)
    cartItems = data['cartItems']

    products=Product.objects.all()
    context= {'products': products, 'cartItems':cartItems}    
    return render(request, 'store/store.html', context)

class  SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('store')
    template_name = 'registration/signup.html'

    def form_valid(self, form):
        view=super(SignUp,self).form_valid(form)
        username, password = form.cleaned_data.get('username'), form.cleaned_data.get('password1')        
        customer = self.user.customer
        user = authenticate(username=username,password=password)
        login(self.request,user,customer)
        return view




def cart(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context= {'items': items, 'order':order,'cartItems':cartItems}
    return render(request, 'store/cart.html', context)

def checkout(request):
    
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context= {'items': items, 'order':order,'cartItems':cartItems}
    return render(request, 'store/checkout.html', context)

def updateItem(request):
    data=json.loads(request.body)
    productId=data['productId']
    action=data['action']

    print('Action:',action)
    print('productId:',productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem,created = OrderItem.objects.get_or_create(order=order , product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity+1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity-1)

    orderItem.save()
    
    if orderItem.quantity <=0:
        orderItem.delete()

    return JsonResponse('Item was added' , safe=False)

#from django.views.decorators.csrf import csrf_protect
#@csrf_protect
def processOrder(request):
    transaction_id=datetime.datetime.now().timestamp()
    data=json.loads(request.body)

    if request.user.is_authenticated:
        customer =request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        
        

    else:
        customer, order = guestOrder(request,data)
        
    total=float(data['form']['total'])
    order.transaction_id=transaction_id

    if total == order.get_cart_total:
        order.complete = True
    order.save()

    if order.shipping == True:
            ShippingAddress.objects.create(
                customer = customer,
                order = order,
                address = data['shipping']['address'],
                city = data['shipping']['city'],
                state = data['shipping']['state'],
                zipcode = data['shipping']['zipcode'],
            )

    return JsonResponse('Payment complete!!',safe=False)
    