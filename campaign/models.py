# Import the necessary module from Django's database package
from django.db import models

# Define the Candidate model, representing a political candidate
class Candidate(models.Model):
    # Define a character field for the candidate's name with a maximum length of 100 characters
    name = models.CharField(max_length=100)
    
    # Define a text field for the candidate's biography
    bio = models.TextField()
    
    # Define a character field for the candidate's political party with a maximum length of 100 characters
    party = models.CharField(max_length=100)
    
    # Define a URL field for the candidate's website
    website = models.URLField()
    
    # Define an image field for the candidate's picture, with images uploaded to the 'candidates/' directory
    image = models.ImageField(upload_to='candidates/')

    # Define the string representation of the model, returning the candidate's name
    def __str__(self):
        return self.name

# Define the CampaignEvent model, representing events associated with a candidate's campaign
class CampaignEvent(models.Model):
    # Define a character field for the event's title with a maximum length of 200 characters
    title = models.CharField(max_length=200)
    
    # Define a text field for the event's description
    description = models.TextField()
    
    # Define a datetime field for the event's date and time
    date = models.DateTimeField()
    
    # Define a character field for the event's location with a maximum length of 200 characters
    location = models.CharField(max_length=200)
    
    # Define a foreign key relationship to the Candidate model, with cascading delete behavior
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)

    # Define the string representation of the model, returning the event's title
    def __str__(self):
        return self.title

# Define the Volunteer model, representing volunteers working for a candidate
class Volunteer(models.Model):
    # Define a character field for the volunteer's name with a maximum length of 100 characters
    name = models.CharField(max_length=100)
    
    # Define an email field for the volunteer's email address
    email = models.EmailField()
    
    # Define a character field for the volunteer's phone number with a maximum length of 15 characters
    phone = models.CharField(max_length=15)
    
    # Define a foreign key relationship to the Candidate model, with cascading delete behavior
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    
    # Define a datetime field that automatically sets the date and time when a record is created
    created_at = models.DateTimeField(auto_now_add=True)

    # Define the string representation of the model, returning the volunteer's name and associated candidate's name
    def __str__(self):
        return f"{self.name} - {self.candidate.name}"
