"""
Models and managers for generic visits.
"""

from datetime import datetime, timedelta

from django.db import models
from django.utils.translation import ugettext_lazy as _
from visits_counter import settings

##########
# Models #
##########

class Visit(models.Model):
    """
    A visit.
    """
    ip_address = models.CharField(max_length=20)
    user_agent = models.CharField(max_length=255)
    object_id = models.CharField(max_length=255)
    object_model = models.CharField(max_length=255)
    time = models.DateTimeField()

    def save(self, *args, **kwargs):
        if self.id:
            super(Visit, self).save(*args, **kwargs)
        else:
            visits = Visit.objects.filter(ip_address=self.ip_address)
            visits = visits.filter(user_agent=self.user_agent)
            visits = visits.filter(object_model=self.object_model)
            visits = visits.filter(object_id=self.object_id)
            visits = visits.filter(time__gt=self.time-timedelta(minutes=settings.MIN_TIME_BETWEEN_VISITS))
            if len(visits)==0:
                super(Visit, self).save(*args, **kwargs)

    class Meta:
        ordering = ('object_model','object_id')
        verbose_name = _('visit')
        verbose_name_plural = _('visits')

    def __unicode__(self):
        return u":".join([self.object_model,str(self.object_id),self.ip_address])
