from django.db import models

# Create your models here.
class Users(models.Model):
    GENDER = (
        ('Male','Male'),
        ('Female','Female'),
    
    )
    ROLES = (
        ('Expert','Expert'),
        ('Farmer','Farmer'),
    
    )
    National_ID = models.CharField(max_length=10,primary_key=True,null=False)
    role = models.CharField(max_length=50,null=True,choices=ROLES)
    first_name = models.CharField(max_length=50,null=True)
    last_name = models.CharField(max_length=50,null=True)
    phone = models.CharField(max_length=50,null=True)
    gender = models.CharField(max_length=50,null=True,choices=GENDER)
    last_name = models.CharField(max_length=50,null=True)
    date_created = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.first_name