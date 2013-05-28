from django.db import models
from django.contrib.auth.models import User

class Marriage(models.Model):
    user = models.ForeignKey(User)
    spouse = models.CharField(max_length=50)

    def __unicode__(self):
        return '%s: %s' % (self.user.username, self.spouse)
