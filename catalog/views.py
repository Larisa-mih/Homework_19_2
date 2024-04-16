from django.shortcuts import render
from django.views.generic import ListView, DetailView

from catalog.models import Product, Contacts, Feedback


def index_contacts(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        feedback = Feedback(name=name, phone=phone, message=message)
        feedback.save()
        with open('data.txt', 'a', encoding='UTF-8') as f:
            f.write(f'{name} ({phone}): {message}' + '\n')

    contacts = Contacts.objects.all()
    return render(request, 'catalog/index_contacts.html', {'contacts': contacts})


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_info.html'


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/index_home.html'
