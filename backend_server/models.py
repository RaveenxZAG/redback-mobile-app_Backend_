from django.db import models
from django.utils import timezone


# Defines a Django model named Users
class Users(models.Model):
    # Defines a field 'username' of type CharField with a maximum length of 20 characters
    username = models.CharField(max_length=20)
    
    # Defines a field 'password' of type CharField with a maximum length of 20 characters
    password = models.CharField(max_length=20)

class warehouse(models.Model):
    email = models.CharField(max_length=50, null=True)
    username = models.CharField(max_length=20, null=True)
    password = models.CharField(max_length=20, null=True)


class acc_details(models.Model):
    email = models.CharField(max_length=50, null=True)
    username = models.CharField(max_length=20, null=True)
    name = models.CharField(max_length=50, default="", blank=True)  # Add default value here
    surname = models.CharField(max_length=50, blank=True)
    dob = models.DateField(null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True) 
    image = models.ImageField(null=True, blank=True,upload_to='images/')


# Class for Help Center messages
class messages(models.Model):
    GENERAL_INQUIRY = 'General Inquiry'
    TECHNICAL_SUPPORT = 'Technical Support'
    BILLING_ISSUE = 'Billing Issue'
    OTHER = 'Other'
    TOPIC_CHOICES = [
        (GENERAL_INQUIRY, 'General Inquiry'),
        (TECHNICAL_SUPPORT, 'Technical Support'),
        (BILLING_ISSUE, 'Billing Issue'),
        (OTHER, 'Other'),
    ]

    OPEN = 'Open'
    RESOLVED = 'Resolved'
    STATUS_CHOICES = [
        (OPEN, 'Open'),
        (RESOLVED, 'Resolved'),
    ]

    AWAITING_REVIEW = 'Awaiting Review'
    RESPONDED = 'Responded'
    ESCALATED = 'Escalated'
    ACTIONS_CHOICES = [
        (AWAITING_REVIEW, 'Awaiting Review'),
        (RESPONDED, 'Responded'),
        (ESCALATED, 'Escalated'),
    ]

    thread_number = models.CharField(max_length=100, unique=True, default='-1') # UUID format, generate in flutter and pass 
    email = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    topic = models.CharField(max_length=30, choices=TOPIC_CHOICES) 
    message_body = models.CharField(max_length=1000)
    timestamp_sent = models.DateTimeField(default=timezone.now,max_length=50)
    timestamp_read = models.DateTimeField(default=timezone.now,max_length=50)
    is_read = models.BooleanField(default=False)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=OPEN)
    actions = models.CharField(max_length=20, choices=ACTIONS_CHOICES, default=AWAITING_REVIEW)

    
   #TODO: create similar class for messages between the app users we added as friends 