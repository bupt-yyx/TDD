from django.shortcuts import render,redirect
from django.http import HttpResponse
from lists.models import Item

# Create your views here.
def home_page(request):
    # if request.method=='POST':
    #     return HttpResponse(request.POST['item_text'])
    if request.method=='POST':
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/lists/the-only-list-in-the-world/')

    items=Item.objects.all()
    return render(request,'home.html',{'items':items})
    # return HttpResponse('<html><title>To-Do lists</title></html>')

def view_list(request):
    items=Item.objects.all()
    return render(request,'home.html',{'items':items})