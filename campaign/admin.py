# Import the necessary module from Django's admin package
from django.contrib import admin

# Import the Candidate model that you want to manage via the Django admin interface
from .models import Candidate

# Register the Candidate model with the Django admin site
# This allows you to add, edit, and delete Candidate instances through the admin interface
admin.site.register(Candidate)
