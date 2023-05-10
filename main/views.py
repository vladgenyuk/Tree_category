from django.shortcuts import render
from .models import Category, Product


def home(request):
    context = {
        'cats_main': Category.objects.filter(level=1).select_related('parent'),
        'products': Product.objects.all(),
        'category': 'zxc'
    }
    # print(context)
    return render(request, 'main/home.html', context)


def details(request, category):
    context = {
        'category': category,
    }
    # print(context)
    return render(request, 'main/details.html', context)


def products(request, category, cat_id):
    context = {
        'products': Product.objects.filter(cat__id=cat_id),
        'category': category,
    }
    return render(request, 'main/products.html', context)


def about(request):
    return render(request, 'main/about.html')


def create_products(request):
    for x in [5, 6, 7, 8, 9, 10, 11, 12, 13, 17, 19]:
        cat = Category.objects.get(id=x)
        for i in range(1):
            Product.objects.create(title=cat.title + " " + str(i), cat_id=x, description='Fake description', cost=100*i + 100)

    return render(request, 'main/create_1.html')
