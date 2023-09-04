from django.shortcuts import render


def index_view(request):
    return render(request, 'website/index.html')


def inner_view(requset):
    return render(requset, 'website/inner-page.html')


def portfolio_view(requset):
    return render(requset, 'website/portfolio-details.html')
