# Import the path function to define URL patterns
from django.urls import path

# Import the views module from the current application
from . import views

# Import Django's built-in authentication views for login and logout
from django.contrib.auth.views import LoginView, LogoutView

# Define the URL patterns for the application
urlpatterns = [
    # Root URL - maps to the home view, accessible at the site's base URL
    path('', views.home, name='home'),
    
    # Events page - maps to the events view, accessible at /events/
    path('events/', views.events, name='events'),
    
    # Volunteer form page - maps to the volunteer view, accessible at /volunteer/
    path('volunteer/', views.volunteer, name='volunteer'),
    
    # Volunteer success page - maps to the volunteer_success view, accessible at /volunteer/success/
    path('volunteer/success/', views.volunteer_success, name='volunteer_success'),
    
    # User registration page - maps to the register view, accessible at /register/
    path('register/', views.register, name='register'),
    
    # Login page - uses Django's built-in LoginView, accessible at /login/
    path('login/', LoginView.as_view(), name='login'),
    
    # Logout page - maps to the logout_view, accessible at /logout/
    path('logout/', views.logout_view, name='logout'),
    
    # User profile page - maps to the profile view, accessible at /accounts/profile/
    path('accounts/profile/', views.profile, name='profile'),
]
