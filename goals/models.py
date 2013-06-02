from django.db import models
from django.contrib.auth.models import User

class DailyGoal(models.Model):
    user = models.ForeignKey(User)
    statement = models.CharField(max_length=500)

    def __unicode__(self):
        return '%s: %s' % (self.user.username, self.statement)

    def count_streaks(self):
        statuses = DailyGoalStatus.objects.filter(daily_goal=self).order_by('date').values_list('status', flat=True)
        previous = None
        count = 0
        true_streaks = []
        false_streaks = []
        last = len(statuses) - 1
        for i, status in enumerate(statuses):
            
            if previous is None:
                print 'previous is none', i, status
                count = 1
                previous = status
            elif previous == status and not i == last:
                previous = status
                print 'previous == status', i, status, previous
                count += 1
            elif previous == status and i == last:   
                previous = status
                print 'previous == status', i, status, previous
                count += 1 
                if previous == True:
                    print '    true streaks updated'
                    true_streaks.append(count)
                else:
                    print '    false streaks updated'
                    false_streaks.append(count)
            elif previous != status:
                print 'previous != status', i, status, previous
                
                if previous == True:
                    print '    true streaks updated'
                    true_streaks.append(count)
                else:
                    print '    false streaks updated'
                    false_streaks.append(count)
                count = 1
                previous = status 
        max_true_streaks = max(true_streaks) if len(true_streaks) else 0
        max_false_streaks = max(false_streaks) if len(false_streaks) else 0
        return {'true_streaks': true_streaks, 'true_streak_record': max_true_streaks, 'false_streaks': false_streaks,  'false_streak_record': max_false_streaks}

class DailyGoalStatus(models.Model):
    daily_goal = models.ForeignKey(DailyGoal)
    date = models.DateField()
    status = models.BooleanField()

    def __unicode__(self):
        return '%s: %s %s %s' % (self.daily_goal.user.username, self.daily_goal.statement, self.date, self.status)

