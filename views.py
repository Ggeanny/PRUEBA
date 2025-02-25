from django.shortcuts import render, redirect
from .models import Inventory
from .forms import InventoryForm

# Create your views here.
def item_list(request):
    items = Inventory.objects.all()
    return render(request, 'inventory/item_list.html', {'items': items})

def item_create(request):
    form = InventoryForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('item_list')
    return render(request, 'inventory/item_form.html', {'form': form})

def item_update(request, id):
    item = Inventory.objects.get(id=id)
    form = InventoryForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('item_list')
    return render(request, 'inventory/item_form.html', {'form': form})

def item_delete(request, id):
    item = Inventory.objects.get(id=id)
    if request.method == 'POST':
        item.delete()
        return redirect('item_list')
    return render(request, 'inventory/item_confirm_delete.html', {'item': item})

