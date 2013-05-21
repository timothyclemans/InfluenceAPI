from django.db import models

class Superpower(models.Model):
    superpower = models.CharField(max_length=50, unique=True)
    color = models.CharField(max_length=50, blank=True, null=True)
    
    def __unicode__(self):
        return self.superpower
        
