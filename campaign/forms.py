# Import the necessary modules from Django's forms package
from django import forms

# Import the Volunteer and Candidate models that will be used in the form
from .models import Volunteer, Candidate

# Define a form class for the Volunteer model, inheriting from forms.ModelForm
class VolunteerForm(forms.ModelForm):
    
    # The Meta class specifies metadata options for the form
    class Meta:
        # Specify the model that this form is associated with
        model = Volunteer
        
        # Define the fields from the Volunteer model that will be included in the form
        fields = ['name', 'email', 'phone', 'candidate']
        
        # Customize the widgets (input elements) for the fields in the form
        widgets = {
            # The 'candidate' field is displayed as a select dropdown with the class 'form-control'
            'candidate': forms.Select(attrs={'class': 'form-control'}),
        }
