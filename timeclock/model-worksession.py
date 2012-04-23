class WorkSession(models.Model):
    """A time period (timedelta) of work on a ticket by a person. """

    start_punch = models.ForeignKey(ClockPunch)
    end_punch = models.ForeignKey(ClockPunch)
    job = models.ForeignKey(Activity)
    worker = models.ForeignKey(Worker)

    def _duration():
      return end_punch.timestamp - start_punch.timestamp
    duration = property(_duration)

    class Meta:
        ordering = ['',]
        verbose_name, verbose_name_plural = "Work Session", "Work SessionStorage"

    def __unicode__(self):
        return "%s" % (self.ticket)

    @models.permalink
    def get_absolute_url(self):
        return ('')