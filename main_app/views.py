from django.core.paginator import Paginator, EmptyPage
from django.shortcuts import render

from main_app.models import Fundraiser


# Create your views here.


def home(request):

    return render(request, 'home.html')

def fundraisers(request):
    data = Fundraiser.objects.all().order_by('id').values()  # ORM select * from customers
    paginator = Paginator(data, 15)
    page = request.GET.get('page', 1)
    try:
        paginated_data = paginator.page(page)
    except  EmptyPage:
        paginated_data = paginator.page(1)
    return render(request, "fundraisers.html", {"data": paginated_data})


def about(request):
    return render(request, 'about.html')


def projects(request):
    return render(request,'projects.html')