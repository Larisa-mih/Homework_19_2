from django.shortcuts import render


def index_contacts(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        with open('data.txt', 'a', encoding='UTF-8') as f:
            f.write(f'{name} ({phone}): {message}' + '\n')

    return render(request, 'catalog/index_contacts.html')


def index_home(request):
    return render(request, 'catalog/index_home.html')
