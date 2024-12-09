from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage
from django.shortcuts import render, redirect, get_object_or_404

from main_app.models import Fundraiser, Donation
from main_app.app_forms import FundraiserForm, DonationForm


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


def add_donation(request, fundraiser_id):
    fundraiser = get_object_or_404(Fundraiser, id=fundraiser_id)
    if request.method == "POST":
        form = DonationForm(request.POST)
        if form.is_valid():
            amount = form.cleaned_data['amount']
            donate = Donation(amount=amount, status=True, fundraiser=fundraiser)
            donate.save()
            messages.success(request, 'Your donation has been successfully saved')
            return redirect('donations')
    else:
        form = DonationForm()
    return render(request, 'donation_form.html', {"form": form, "fundraiser": fundraiser})


def donations(request):
    data = Donation.objects.all().order_by('id').values()  # ORM to select all donations
    paginator = Paginator(data, 15)
    page = request.GET.get('page', 1)
    try:
        paginated_data = paginator.page(page)
    except EmptyPage:
        paginated_data = paginator.page(1)

    return render(request, "donations.html", {"data": paginated_data})
