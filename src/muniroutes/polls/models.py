from django.db import models
import datetime

class Poll(models.Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __unicode__(self):
       return self.question

    def was_published_today(self):
       return self.pub_date.date() == datetime.date.today()
    was_published_today.short_description = 'Published today?'


class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    choice = models.CharField(max_length=200)
    votes = models.IntegerField()

    def __unicode__(self):
       return self.choice

class Stops(models.Model):
    tag = models.IntegerField()
    title = models.CharField(max_length=128)
    lat = models.FloatField()
    lon = models.FloatField()
    stopId = models.IntegerField()
    route = models.CharField(max_length=16)
    
    def __unicode__(self):
        return u'%s %s' % (self.route, self.title)
        
class BusLoc(models.Model):
    vehId = models.IntegerField()
    routeTag = models.CharField(max_length=16)
    dirTag = models.CharField(max_length=32)
    lat = models.FloatField()
    lon = models.FloatField()
    secsSinceReport = models.IntegerField()
    predictable = models.CharField(max_length=16)
    
    def __unicode__(self):
        return u'%s %s' % (self.id, self.routeTag)

