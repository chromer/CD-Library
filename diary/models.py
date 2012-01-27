from datetime import datetime
from django.db import models
from django.contrib.auth.models import User


class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    timestamp = models.DateTimeField(default=datetime.now)
    author = models.ForeignKey(User)
    ups = models.ManyToManyField(User, related_name='ups', null=True, blank=True)

    def get_ups(self):
        return self.ups.all().count()

    def get_time(self):
        return self.timestamp.strftime('%I:%M %p')

    def __unicode__(self):
        return '%s- %s on %s'%(self.author.username, self.title, self.timestamp.date())

