from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

CATEGORIES = (
    ('IP', 'Interview Prep'),
    ('CC', 'Coding Challenge'),
    ('AL', 'Algorithms'),
    ('DS', 'Data Structures'),
    ('CS', 'Cheat Sheets'),
    ('RT', 'Resume Tips'),
    ('HR', 'Hiring Resources'),
)

class Resource(models.Model):
    category = models.CharField(
        max_length=2,
        choices=CATEGORIES,
        default=CATEGORIES[0][0],
    )
    title = models.CharField(max_length=150)
    content = models.CharField(max_length=999)
    resource_url = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}"
    
    def get_absolute_url(self):
        return reverse('resources_index')
# Create your models here.



class JobApp(models.Model):
    company = models.CharField(max_length=100)
    job_title = models.CharField(max_length=50)
    submission_date = models.DateField('Submission Date')
    follow_up_date = models.DateField('Follow-Up Date')
    job_post_url = models.CharField(max_length=999)
    description = models.CharField(max_length=256)
    notes = models.CharField(max_length=256)
    excitement_level = models.IntegerField()
    resume_url = models.CharField(max_length=999)
    cover_letter_url = models.CharField(max_length=999)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"App for {self.company}"

    def get_absolute_url(self):
        return reverse('jobapps_index')



class Comment(models.Model):
    content = models.CharField(max_length=140)
    comment_date = models.DateField('Comment Posted On:')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.content}"

    class Meta:
        ordering=['-comment_date']

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE)