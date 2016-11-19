from __future__ import unicode_literals

from django.db import models

class User(models.Model):
    username = models.CharField(max_length = 30, unique=True, blank=False)
    password = models.CharField(max_length = 30, blank=False)
    createddate = models.DateTimeField(auto_now_add=True)
    updateddate = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.username
