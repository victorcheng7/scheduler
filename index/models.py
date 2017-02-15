from __future__ import unicode_literals
from django.utils import timezone
from datetime import datetime
from django.db.models.fields import TimeField, IntegerField

from django.db import models
from django.contrib.auth.models import User



# Create your models here.
DAY_OF_THE_WEEK = (
    ('MO', 'Monday'),
    ('TU', 'Tuesday'),
    ('WE', 'Wednesday'),
    ('TH', 'Thursday'),
    ('FR', 'Friday'),
)
class Profile(models.Model):
    private = models.BooleanField(default=False) # OPTIONAL Hide schedule from others? implement last
    bot = models.BooleanField(default=False)

    user = models.OneToOneField(User)
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)

    def __unicode__(self):
        return self.firstName



class Class(models.Model):
    current = models.BooleanField(default=False) #Is this a class they're taking right now?
    comfortable = models.BooleanField(default=False) #Are they comfortable with the class? OPTIONAL

    QUARTER = (
        ('FA', 'Fall'),
        ('SP', 'Spring'),
        ('WI', 'Winter'),
    )
    department = models.CharField(max_length=50)
    classTitle = models.CharField(max_length=50) # ex. CS130a data structures and algorithms

    time_start = models.TimeField(blank=True) #MULTIPLE START TIMES AND DAYS OF WEEK
    time_end = models.TimeField(blank=True)
    dayOfWeek1 = models.CharField(
        max_length=2,
        choices=DAY_OF_THE_WEEK
    )
    dayOfWeek2 = models.CharField(
        max_length=2,
        choices=DAY_OF_THE_WEEK
    )

    quarter = models.CharField(
        max_length=6,
        choices=QUARTER
    )
    code = models.CharField(max_length=6)

    instructor = models.CharField(max_length=40, blank=True)
    location = models.CharField(max_length=40, blank=True)
    units = models.IntegerField(default=4)

    spaceLeft = models.IntegerField(blank=True)
    classSize = models.IntegerField(blank=True)
    courseDescription = models.TextField(blank=True)

    user = models.ManyToManyField(Profile, related_name='classes')  #Profile.classes.all() to get all classes for a user

    def __unicode__(self):
        return self.classTitle

    def save(self, *args, **kwargs):
        update_fields(self)
        return super(Class, self).save(*args, **kwargs)


class Section(models.Model):
    spaceLeft = models.IntegerField(blank=True)
    classSize = models.IntegerField(blank=True)
    code = models.IntegerField()
    time_start = models.TimeField()  # MULTIPLE START TIMES AND DAYS OF WEEK
    time_end = models.TimeField()
    dayOfWeek1 = models.CharField(
        max_length=2,
        choices=DAY_OF_THE_WEEK
    )
    course = models.ForeignKey(Class, on_delete=models.CASCADE, related_name='sections')


    def save(self, *args, **kwargs):
        update_fields(self)
        return super(Section, self).save(*args, **kwargs)

class Major(models.Model):
    units = models.IntegerField(blank=True, default=180)
    requirements = models.ManyToManyField(Class, related_name='required_for_major')
    users = models.ManyToManyField(Profile, related_name='major')

    def save(self, *args, **kwargs):
        update_fields(self)
        return super(Major, self).save(*args, **kwargs)

    #Include prerequirsites for every class.