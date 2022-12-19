from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from datetime import datetime

# Create your models here.
class Account(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    TITLE_CHOICES = (("Mr", "Mr"), ("Ms", "Ms"), ("Mrs", "Mrs"),)
    title = models.CharField(max_length = 3, choices = TITLE_CHOICES, default = 'Mr')
    @property
    def short_name(self):
        if self.first_name and self.last_name:
            return "%s%s" % (self.first_name[:1],self.last_name[:1])
    def __str__(self):
        return f'{self.user.username} Account'

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    contact = models.CharField(max_length=10, null=True)
    contact_ext = models.CharField(max_length=3, null=True)
    join_date = models.DateTimeField(default=datetime.now, blank=True)
    join_dateformat = models.CharField(max_length=10,default="D-M-Y")
    team = models.CharField(max_length=20)
    jobtitle = models.CharField(max_length=20)
    lastlogin = models.DateTimeField(auto_now=True)
    loggedIn = models.BooleanField(default=False)
    dateformat = models.CharField(max_length=20,default="Y-M-D h:m:s")
    picture = models.ImageField(default='default.jpg',upload_to='profile_pics')
    
    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self,**kwargs):
        super().save()
        img = Image.open(self.picture.path)
        if (img.height > 300) or (img.width > 300):
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.picture.path)
