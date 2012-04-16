import datetime

from django.core.management.base import BaseCommand, CommandError

from timeclock.models import ClockPunch, Activity


class Command(BaseCommand):
    args = '<>'
    help = 'List ClockPunches'

    def handle(self, *args, **options):

      break_event = Activity.objects.get(ticket="Break")
      dates = ClockPunch.objects.dates('timestamp','day')
      print break_event.pk

#       for day in dates:
#         print day
#         for punch in ClockPunch.objects.filter(timestamp__range=(day,day + datetime.timedelta(1))).order_by('timestamp'):
#           print "    %s %s \t %3s: %s" % (punch.timestamp.strftime("%H:%M"), punch.worker, punch.activity.pk, punch.activity)


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