from django.shortcuts import render, redirect, get_object_or_404
from product.models import Product
from .form import CreateForm

# Create your views here.

def home(request):
    obj = Product.objects.all()
    context={
        'object':obj
    }
    return render(request, 'index.html', context)

def product(request):
    obj = Product.objects.all()
    
    context={
        'object':obj
    }
    return render(request, 'product.html', context)
# def productDetail(request):
#     obj = Product.objects.get(id=1)
#     context={
#         'object': obj
#     }
#     return render(request, 'product.html', context)


def createform(request):
    form = CreateForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save() 
        form = CreateForm()
            
    context = {
        'form' : form
    }
    # context['form']= form
    return render(request, 'form.html', context)

def updateform(request,id):
    obj = get_object_or_404(Product, id=id)
    print(obj)
    form = CreateForm(request.POST or None,instance = obj)
    print(form)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, 'form.html', context)

def dynamic_lookup_view(request, id):
    # obj = Product.objects.get(id=id)
    obj = get_object_or_404(Product, id=id)
    context={
        'object': obj
    }
    print(obj)
    return render(request, 'productDetail.html ', context)


def product_delete(request, id):
    try:
        # obj = Product.objects.get(id=id)
        obj = get_object_or_404(Product, id=id)
        obj.delete()
        return redirect('../')
    except:
        pass
    # context={
    #     'object': obj
    # }
    # print(obj)
    return render(request, 'productDetail.html')
