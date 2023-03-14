from django.db import models

# Create your models here.
from django.contrib.auth.models import User
class contents(models.Model):
    level = models.IntegerField(default=0,null=True)
    sno = models.AutoField(primary_key=True)
    slug = models.CharField(default="",max_length=1000)
    link = models.TextField(default="")
    def __str__(self) -> str:
        return f"Level {self.level}"


class thumbnail(models.Model):
    card_number = models.IntegerField(null=True)
    sno = models.AutoField(primary_key=True)
    slug = models.ForeignKey(contents,models.CASCADE,default = "")
    level = models.CharField(default=None,max_length=100)
    course_image = models.ImageField(upload_to="thumbnails")
    

    def __str__(self) -> str:
        return self.level
    

    
    
class UserPermissions(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    card1 = models.BooleanField(default=False)
    card2 = models.BooleanField(default=False)
    card3 = models.BooleanField(default=False)
    card4 = models.BooleanField(default=False)
    card5 = models.BooleanField(default=False)
    card6 = models.BooleanField(default=False)
    card7 = models.BooleanField(default=False)
    card8 = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username}'s permissions"
    
