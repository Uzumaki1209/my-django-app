from django.db import models


class Candidate(models.Model):
    """
    Represents a political candidate.

    Attributes:
        name (str): The name of the candidate.
        bio (str): The biography of the candidate.
        party (str): The political party of the candidate.
        website (str): The website URL of the candidate.
        image (ImageField): The image of the candidate.
    """
    name = models.CharField(max_length=100)
    bio = models.TextField()
    party = models.CharField(max_length=100)
    website = models.URLField()
    image = models.ImageField(upload_to='candidates/')

    def __str__(self):
        return self.name


class CampaignEvent(models.Model):
    """
    Represents an event associated with a candidate's campaign.

    Attributes:
        title (str): The title of the campaign event.
        description (str): The description of the campaign event.
        date (datetime): The date and time of the campaign event.
        location (str): The location of the campaign event.
        candidate (ForeignKey): A foreign key to the Candidate model.
    """
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField()
    location = models.CharField(max_length=200)
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Volunteer(models.Model):
    """
    Represents a volunteer working for a candidate.

    Attributes:
        name (str): The name of the volunteer.
        email (EmailField): The email address of the volunteer.
        phone (str): The phone number of the volunteer.
        candidate (ForeignKey): A foreign key to the Candidate model.
        created_at (datetime): The date and time when the record was created.
    """
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.candidate.name}"
