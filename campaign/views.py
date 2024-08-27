# Import the necessary functions and models from Django and the current application
from django.shortcuts import render, redirect
from .models import Candidate, CampaignEvent, Volunteer
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from .forms import VolunteerForm

# View function for the home page
def home(request):
    # Get the first candidate from the database
    candidate = Candidate.objects.first()
    
    # Render the home page template with the candidate's information
    return render(request, 'campaign/home.html', {'candidate': candidate})

# View function for the events page
def events(request):
    # Get all campaign events from the database
    events = CampaignEvent.objects.all()
    
    # Render the events page template with the list of events
    return render(request, 'campaign/events.html', {'events': events})

# View function for the volunteer form page
def volunteer(request):
    # Check if the request method is POST (form submission)
    if request.method == 'POST':
        # Create a form instance with the submitted data
        form = VolunteerForm(request.POST)
        
        # Validate the form data
        if form.is_valid():
            # Save the form data to the database
            form.save()
            
            # Redirect to the volunteer success page
            return redirect('volunteer_success')
    else:
        # If the request is not POST, create a blank form instance
        form = VolunteerForm()

    # Render the volunteer form page template with the form instance
    return render(request, 'campaign/volunteer.html', {'form': form})

# View function for user registration
def register(request):
    # Check if the request method is POST (form submission)
    if request.method == 'POST':
        # Create a form instance with the submitted data
        form = UserCreationForm(request.POST)
        
        # Validate the form data
        if form.is_valid():
            # Save the user data to the database
            user = form.save()
            
            # Log the user in
            login(request, user)
            
            # Redirect to the home page
            return redirect('home')
    else:
        # If the request is not POST, create a blank form instance
        form = UserCreationForm()

    # Render the registration page template with the form instance
    return render(request, 'campaign/register.html', {'form': form})

# View function to log out a user
def logout_view(request):
    # Log the user out
    logout(request)
    
    # Redirect to the homepage
    return redirect('/')

# View function for the user's profile page
def profile(request):
    # Render the profile page template
    return render(request, 'campaign/profile.html')

# View function for the volunteer success page
def volunteer_success(request):
    # Render the volunteer success page template
    return render(request, 'campaign/volunteer_success.html')
