from django.shortcuts import redirect, render
from django.http import HttpResponse
from lists.models import Item

# Create your views here.
def home_page(request):
    '''Домашня страница'''
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/lists/одинонокий список/')

    items = Item.objects.all()
    return render(request, 'home.html', {'items': items})
