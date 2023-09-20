# signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import BloodRequest

@receiver(post_save, sender=BloodRequest)
def send_notification_to_donor(sender, instance, created, **kwargs):
    if created:
        # Notify the donor about the new request (you can use your preferred notification method)
        # Example: send a notification to the donor's email
        subject = f'New Blood Request from {instance.requester.username}'
        message = f'You have a new blood request from {instance.requester.username}. Please check your dashboard.'
        # Send email or use messaging framework to send the notification
