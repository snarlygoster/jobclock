import datetime
from collections import defaultdict

from django.core.management.base import BaseCommand, CommandError

from timeclock.models import ClockPunch, Activity


class Command(BaseCommand):
    args = '<>'
    help = 'List ClockPunches'

    def handle(self, *args, **options):

      break_event = Activity.objects.get(ticket="Break")
      dates = ClockPunch.objects.dates('timestamp','day')
      print break_event.pk
      punches = ClockPunch.objects.all().order_by('timestamp')
      print punches.count()
      scoreboard = {}
      work_periods = defaultdict(list)
      for punch in punches:
        if punch.worker not in scoreboard:
          scoreboard[punch.worker] = {"start" : punch.timestamp, 'job' : punch.activity}
        else:
          duration = punch.timestamp - scoreboard[punch.worker]['start']
          work_periods[punch.activity].append(duration)
          if punch.activity == break_event:
            del scoreboard[punch.worker]
          else:
            scoreboard[punch.worker] = {"start" : punch.timestamp, 'job' : punch.activity}

      for job, durations in work_periods.iteritems():
        self.stdout.write("%s - %s \n" % (job, [str(duration) for duration in work_periods[job] ] ) )

        #self.stdout.write("   %s %s \t %3s: %s\n" % (punch.timestamp.strftime("%m/%d %H:%M"), punch.worker, punch.activity.pk, punch.activity))

#       for day in dates:
#         print day
#         for punch in ClockPunch.objects.filter(timestamp__range=(day,day + datetime.timedelta(1))).order_by('timestamp'):
#           print "    %s %s \t %3s: %s\n" % (punch.timestamp.strftime("%H:%M"), punch.worker, punch.activity.pk, punch.activity)


#         for poll_id in args:
#             try:
#                 poll = Poll.objects.get(pk=int(poll_id))
#             except Poll.DoesNotExist:
#                 raise CommandError('Poll "%s" does not exist' % poll_id)
#
#             poll.opened = False
#             poll.save()
#
#             self.stdout.write('Successfully closed poll "%s"\n' % poll_id)