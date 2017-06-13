from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item

# Create your views here.
def home_page(request):
    # return HttpResponse("<html><title>To-Do lists</title></html>")
    if request.method == "POST":
        # return HttpResponse(request.POST['item_text'])
        new_item_text = request.POST.get('item_text')
        Item.objects.create(text=new_item_text)
        return redirect('/lists/the-only-list-in-the-world/')
    return render(request, 'lists/home.html')

def view_lists(request):
    items = Item.objects.all()
    return render(request, 'lists/list.html', {"items": items})
