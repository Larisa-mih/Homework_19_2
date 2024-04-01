from django.shortcuts import render
from catalog.models import Product, Contacts

def index_contacts(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        with open('data.txt', 'a', encoding='UTF-8') as f:
            f.write(f'{name} ({phone}): {message}' + '\n')

    contacts = Contacts.objects.all()
    return render(request, 'catalog/index_contacts.html', {'contacts': contacts})


def index_home(request):
    top_products = Product.objects.order_by('-created_at')[:5]
    for product in top_products:
        print(f'{product.name} {product.price}')
    return render(request, 'catalog/index_home.html', {'top_products': top_products})
