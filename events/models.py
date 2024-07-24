from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Event(models.Model):
    EVENT_TYPE_CHOICES = [
        ('conference','Conference'),
        ('seminar','Seminar'),
        ('workshop','Workshop')
    ]
    STATUS_CHOICES = [
        ('approve','Approve'),
        ('decline','Decline'),
        ('pending','Pending')
    ]
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    type = models.CharField(choices=EVENT_TYPE_CHOICES,max_length=50)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    status = models.CharField(choices=STATUS_CHOICES,default='Pending',max_length=50,null=True)
    admin_comment = models.TextField(null=True,blank=True)
    date_created = models.DateField(auto_now_add=True)


