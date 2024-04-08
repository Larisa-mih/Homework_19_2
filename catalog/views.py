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
    context = {
        'object_list': Product.objects.all(),
        'title': 'Интернет магазин цифровой и бытовой техники - Главная'
    }
    return render(request, 'catalog/index_home.html', context)


def product(request, pk):
    product_item = Product.objects.get(pk=pk)
    context = {
        'object_list': Product.objects.filter(category=pk),
        'product_item': product_item,
        'title': f'Интернет магазин цифровой и бытовой техники - Информация по товару {product_item.name}'
    }
    return render(request, 'catalog/product_info.html', context)
