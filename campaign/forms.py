from django import forms
from .models import Volunteer, Candidate


class VolunteerForm(forms.ModelForm):
    """
    Form for adding and editing volunteers associated with a candidate.

    Meta:
        model (Model): The model that this form is associated with.
        fields (list): The fields to be included in the form.
        widgets (dict): Custom widgets for form fields.
    """
    class Meta:
        model = Volunteer
        fields = ['name', 'email', 'phone', 'candidate']
        widgets = {
            'candidate': forms.Select(attrs={'class': 'form-control'}),
        }
