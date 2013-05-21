from django.db import models
from django.contrib.auth.models import User

class DailyGoal(models.Model):
    user = models.ForeignKey(User)
    statement = models.CharField(max_length=500)

    def __unicode__(self):
        return '%s: %s' % (self.user.username, self.statement)

class DailyGoalStatus(models.Model):
    daily_goal = models.ForeignKey(DailyGoal)
    date = models.DateField()
    status = models.BooleanField()

    def __unicode__(self):
        return '%s: %s %s %s' % (self.daily_goal.user.username, self.daily_goal.statement, self.date, self.status)

