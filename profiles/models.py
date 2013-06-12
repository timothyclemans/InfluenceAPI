from django.db import models

# Create your models here.

class WordReplacement(models.Model):

    word        = models.CharField(max_length = 15)
    replacement = models.CharField(max_length = 15)

    def __unicode__(self):
        return '%s:%s' % (self.word, self.replacement)
