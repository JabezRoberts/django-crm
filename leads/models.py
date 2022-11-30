from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    pass    


class Lead(models.Model):
    # SOURCE_CHOICES = (
    #     ('YouTube', 'YouTube'),
    #     ('Google', 'Google'),
    #     ('Newsletter', 'Newsletter')
    # )
    
    
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField(default=0)
    agent = models.ForeignKey("Agent", on_delete=models.CASCADE) # this says every lead has an agent, models.CASCADE means if the agent is deleted then the lead is deleted

    
    # phoned = models.BooleanField(default=False)
    # source = models.CharField(choices=SOURCE_CHOICES, max_length=100)
    
    # profile_picture = models.ImageField(blank=True, null=True) # blank is empty string, null is no value. so we can save lead without profile picture
    # special_files = models.FileField(blank=True, null=True)
    



class Agent(models.Model):
    #user = models.ForeignKey(User, on_delete=models.CASCADE) #ForiegnKey creates manay agents for one user. Use one to one field to fix this where one agent has one user
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # lead = models.ForeignKey("Lead", on_delete=models.CASCADE)-> every agent can only have one lead
    