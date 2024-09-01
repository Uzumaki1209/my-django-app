from django.shortcuts import render, redirect
from .models import Candidate, CampaignEvent, Volunteer
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from .forms import VolunteerForm


def home(request):
    """
    Display the home page with candidate information.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered home page with candidate information.
    """
    candidate = Candidate.objects.first()
    return render(request, 'campaign/home.html', {'candidate': candidate})


def events(request):
    """
    Display the events page with a list of campaign events.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered events page with a list of events.
    """
    events = CampaignEvent.objects.all()
    return render(request, 'campaign/events.html', {'events': events})


def volunteer(request):
    """
    Handle the volunteer form submission and display the form page.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered volunteer form page.
    """
    if request.method == 'POST':
        form = VolunteerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('volunteer_success')
    else:
        form = VolunteerForm()

    return render(request, 'campaign/volunteer.html', {'form': form})


def register(request):
    """
    Handle user registration and display the registration form.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered registration form page.
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()

    return render(request, 'campaign/register.html', {'form': form})


def logout_view(request):
    """
    Log out the user and redirect to the homepage.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Redirect to the homepage.
    """
    logout(request)
    return redirect('/')


def profile(request):
    """
    Display the user's profile page.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered profile page.
    """
    return render(request, 'campaign/profile.html')


def volunteer_success(request):
    """
    Display the volunteer success page.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered volunteer success page.
    """
    return render(request, 'campaign/volunteer_success.html')
