from django.shortcuts import render,get_object_or_404
from BookApp.models import Item,Order,OrderItem
from django.shortcuts import redirect
from django.utils import timezone

# Create your views here.

def add_to_cart(request,pk):
    item=get_object_or_404(Item,id=pk)
    order_item,created=OrderItem.objects.get_or_create(
        item=item,
        user=request.user,
        ordered=False   
    )
    order_qs=Order.objects.filter(user=request.user,ordered=False)

    if order_qs.exists():
        order=order_qs[0]
        #check if the order item is in the order
        if order.items.filter(id=item.id).exists():
            order_item.quantity +=1
            order_item.save()
        else:
            order.items.add(order_item)
           

            
    else:
        order_date=timezone.now()
        order=Order.objects.create(user=request.user,ordered_date=order_date)
        order.items.add(order_item)
    
    return redirect('book-detail',pk=pk)
    

def remove_from_cart(request,pk):
    item=get_object_or_404(Item,id=pk)
    order_qs=Order.objects.filter(user=request.user,ordered=False)

    if order_qs.exists():
        order=order_qs[0]
       
    #check if the order item is in the order
        if order.items.filter(id=item.id).exists():
            order_item=OrderItem.objects.filter(item=item,user=request.user,ordered=False)[0]

            order.items.remove(order_item)
        else:

            return redirect('book-detail',pk=pk)
    else:
        return redirect('book-detail',pk=pk)

    return redirect('book-detail',pk=pk)