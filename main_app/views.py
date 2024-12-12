from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required

from django.core.paginator import Paginator, EmptyPage
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404

from main_app.models import Fundraiser, Donation
from main_app.app_forms import FundraiserForm, DonationForm, LoginForm


# Create your views here.

@login_required
def home(request):
    return render(request, 'home.html')

@login_required
def fundraisers(request):
    data = Fundraiser.objects.all().order_by('id').values()  # ORM select * from customers
    paginator = Paginator(data, 15)
    page = request.GET.get('page', 1)
    try:
        paginated_data = paginator.page(page)
    except  EmptyPage:
        paginated_data = paginator.page(1)
    return render(request, "fundraisers.html", {"data": paginated_data})

@login_required
def about(request):
    return render(request, 'about.html')

@login_required
def projects(request):
    return render(request, 'projects.html')

@login_required
@permission_required ("main_app.add_fundraiser", raise_exception=True)
def add_fundraiser(request):
    if request.method == "POST":
        form = FundraiserForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Fundraiser  added  successfully")
            return redirect('fundraisers')
    else:
        form = FundraiserForm()

    return render(request, 'fundraiser_form.html', {"form": form})

@login_required

def add_donation(request, fundraiser_id):
    fundraiser = get_object_or_404(Fundraiser, id=fundraiser_id)
    if request.method == "POST":
        form = DonationForm(request.POST)
        if form.is_valid():
            donation = form.save(commit=False)
            donation.amount = form.cleaned_data['amount']
            donation.project_name = form.cleaned_data['project_name']
            donation.status = True
            donation.fundraiser = fundraiser
            donation.save()
            messages.success(request, 'Your donation has been successfully saved ')
            return redirect('donations')
        else:
            # Handle invalid form, e.g., display error messages
            messages.error(request, 'Please correct the errors in the form.')
            return render(request, 'donation_form.html', {'form': form, 'fundraiser': fundraiser})
    else:
        form = DonationForm()
    return render(request, 'donation_form.html', {'form': form, 'fundraiser': fundraiser})

@login_required
def donations(request):
    data = Donation.objects.all().order_by('id').values()  # ORM to select all donations
    paginator = Paginator(data, 15)
    page = request.GET.get('page', 1)
    try:
        paginated_data = paginator.page(page)
    except EmptyPage:
        paginated_data = paginator.page(1)

    return render(request, "donations.html", {"data": paginated_data})

@login_required
@permission_required("main_app.delete_fundraiser",raise_exception=True)
def delete_fundraiser(request, fundraiser_id):
    fundraiser = Fundraiser.objects.get(id=fundraiser_id)
    fundraiser.delete()
    messages.info(request, f"Fundraiser  {fundraiser.first_name}  was  deleted!! ")
    return redirect('fundraisers')  # Redirects back to customers page and will load again

@login_required
@permission_required("main_app.view_fundraiser", raise_exception=True)
def fundraiser_details(request, fundraiser_id):
    fundraiser = Fundraiser.objects.get(id=fundraiser_id)
    donations = Donation.objects.filter(fundraiser_id=fundraiser_id)

    return render(request, "details.html", {'fundraiser': fundraiser, 'donations': donations})

@login_required
@permission_required("main_app.change_fundraiser", raise_exception=True)
def update_fundraiser(request, fundraiser_id):
    fundraiser = get_object_or_404(Fundraiser, id=fundraiser_id)
    if request.method == "POST":
        form = FundraiserForm(request.POST, request.FILES, instance=fundraiser)
        if form.is_valid():
            form.save()
            messages.success(request, f"Fundraiser {form.cleaned_data['first_name']}   was  updated!")
            return redirect('fundraisers')
    else:
        form = FundraiserForm(instance=fundraiser)
    return render(request, 'fundraiser_update_form.html', {"form": form})

@login_required
@permission_required("main_app.view_fundraiser", raise_exception=True)
def search_fundraiser(request):
    search_term = request.GET.get('search')
    da_ta = Fundraiser.objects.filter(
        Q(first_name__icontains=search_term) | Q(last_name__icontains=search_term) | Q(email__icontains=search_term))
    return render(request, "search.html", {"fundraisers": da_ta})


def login_user(request):
    if request.method == "GET":
        form = LoginForm()
        return render(request , 'login.html',{'form':form})
    elif request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)  #stores this data as sessions in the server and on the broswer as cookies
                return redirect('home')
        # messages.error(request,"Invalid username or password")
        return render(request , 'login.html',{'form':form})

@login_required
def logout_user(request):
    logout(request)
    return redirect('login')