from django.db import models
from django.contrib.auth.models import User

class DailyGoal(models.Model):
    user = models.ForeignKey(User)
    statement = models.CharField(max_length=500)
    started = models.DateField(null=True, blank=True, auto_now_add=True)
    end = models.DateField(null=True, blank=True)

    def __unicode__(self):
        return '%s: %s' % (self.user.username, self.statement)

    def statuses(self):
        return DailyGoalStatus.objects.filter(daily_goal=self).order_by('date').values_list('status', flat=True)

    def raw_statuses(self):
        return DailyGoalStatus.objects.filter(daily_goal=self).order_by('date')

    def achieved_goal(self):
        print 'achieved goal'
        statuses = list(self.statuses())
        print [type(i) for i in statuses]
        print 'status type', type(statuses)
        print statuses
        denominator = len(statuses)
        if denominator == 0:
            return {'numerator': 0, 'denominator': 0, 'percentage': 0}
        print 'denominator', denominator
        numerator = statuses.count(True)
        print 'numerator', numerator
        percentage = int(100 * float(numerator) / float(denominator))
        print percentage
        dictionary = {'numerator': numerator, 'denominator': denominator, 'percentage': percentage}
        print dictionary
        return {'numerator': numerator, 'denominator': denominator, 'percentage': percentage}

    def count_streaks(self):
        statuses = self.statuses()
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
                if i == last:
                    if previous == True:
                        true_streaks.append(1)
                    else:
                        false_streaks.append(1)
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
                if i == last:
                    if previous == True:
                        print '    true streaks updated'
                        true_streaks.append(count)
                    else:
                        print '    false streaks updated'
                        false_streaks.append(count)                   
        max_true_streaks = max(true_streaks) if len(true_streaks) else 0
        max_false_streaks = max(false_streaks) if len(false_streaks) else 0
        return {'true_streaks': true_streaks, 'true_streak_record': max_true_streaks, 'false_streaks': false_streaks,  'false_streak_record': max_false_streaks}

    def essay(self):
        statuses = self.statuses()
        if not statuses:
            statement = self.statement.split(' ')
            if statement[0].endswith('e'):
                statement[0] = statement[0][:-1]
            statement[0] = statement[0].lower() + 'ing'
            statement = ' '.join(statement)
            return 'On %s, Tim set a daily goal of %s. ' % (self.started.strftime('%A, %B %d, %Y'), statement)
        the_essay = ''
        streak_data = self.count_streaks()
        if not self.started:
            self.started = DailyGoalStatus.objects.filter(daily_goal=self).order_by('date')[0].date
        statement = self.statement.split(' ')
        statement[0] = statement[0].lower() + 'ing'
        statement = ' '.join(statement)
        the_essay = 'On %s, Tim set a daily goal of %s. ' % (self.started.strftime('%A, %B %d, %Y'), statement)
        
        def handel_upto_99(number):
            predef={0:"zero",1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine",10:"ten",11:"eleven",12:"twelve",13:"thirteen",14:"fourteen",15:"fifteen",16:"sixteen",17:"seventeen",18:"eighteen",19:"nineteen",20:"twenty",30:"thirty",40:"fourty",50:"fifty",60:"sixty",70:"seventy",80:"eighty",90:"ninety",100:"hundred",100000:"lakh",10000000:"crore",1000000:"million",1000000000:"billion"}
            if number in predef.keys():
                return predef[number]
            else:
                return predef[(number/10)*10]+' '+predef[number%10]
        if not statuses:
            return the_essay
        elif statuses[0]:
            if streak_data['true_streaks'][0] > 1:
                longest_streak = ''
                if streak_data['true_streaks'][0] == max(streak_data['true_streaks']):
                    longest_streak = ', his longest streak'
                the_essay += 'He started out well achieving his daily goal for %s days straight%s. ' % (handel_upto_99(streak_data['true_streaks'][0]), longest_streak)
                
            else:
                the_essay += "He started out well achieving his daily goal on the first day. Unfortantuantly he didn't achive his goal the next day."
        else:
            the_essay += 'He started out poorly not achieving his daily goal on the first day.'
        return the_essay

class DailyGoalStatus(models.Model):
    daily_goal = models.ForeignKey(DailyGoal)
    date = models.DateField()
    status = models.BooleanField()

    def __unicode__(self):
        return '%s: %s %s %s' % (self.daily_goal.user.username, self.daily_goal.statement, self.date, self.status)

