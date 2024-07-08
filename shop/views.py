from django.shortcuts import render

def shop(request):
    return render(request, 'market/index.html')


def contact(request):
    return render(request, 'market/contact.html')


def single_product(request):
    return render(request, 'market/single_product.html')