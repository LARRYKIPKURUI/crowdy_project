from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage
from django.shortcuts import render, redirect

from main_app.models import Fundraiser
from main_app.app_forms import FundraiserForm

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
    return render(request, 'projects.html')


def add_fundraiser(request):
    if request.method == "POST":
        form = FundraiserForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Fundraiser added successfully")
            return redirect('fundraisers')
    else:
        form = FundraiserForm()

    return render(request, 'fundraiser_form.html', {"form": form})

