from django.db import models
from django.contrib.auth.models import User
from rest_framework.response import Response
from base.models import BaseModel


class Account(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=100)
    def __str__(self):
        return str(self.user.first_name)

class Employer(BaseModel):
    phone_number = models.CharField(max_length=25)
    company_name = models.CharField(max_length=1000)
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)


class Joblisting(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)

    
class EducationalResources(BaseModel):
    title = models.CharField(max_length=255)
    content = models.TextField(max_length=1000)
    category = models.CharField(max_length=255)


class SkillAssessment(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField()
    date_taken = models.DateField(auto_now_add=True)
    category = models.ForeignKey(EducationalResources, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return str(self.name)