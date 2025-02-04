from django.shortcuts import render, get_object_or_404, redirect
from .models import Item

def item_list(request):
    items = Item.objects.all()
    return render(request, 'warehouse/item_list.html', {'items': items})

def item_detail(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    return render(request, 'warehouse/item_detail.html', {'item': item})

def update_stock(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    if request.method == 'POST':
        new_stock = request.POST.get('stock') 
        if new_stock.isdigit(): 
            item.stock = int(new_stock)
            item.save()
    return redirect('item_detail', item_id=item.id)

