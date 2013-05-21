from django.db import models
from django.contrib.auth.models import User
from superpowers.models import Superpower
 
class Bucksgiven(models.Model):
    datetime = models.DateTimeField(auto_now_add=True)
    student = models.ForeignKey(User, related_name='student')
    given_by = models.ForeignKey(User, related_name='given_by')
    amount = models.PositiveIntegerField()
    summary = models.TextField()
    superpower_used = models.ForeignKey(Superpower)
    
    def __unicode__(self):
        return '%s: $%s for using %s superpower' % (self.student.get_full_name(), self.amount, self.superpower_used.superpower)
