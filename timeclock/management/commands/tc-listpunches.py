import datetime
import pprint
import csv

from collections import defaultdict

from django.core.management.base import BaseCommand, CommandError

from timeclock.models import ClockPunch, Activity


class Command(BaseCommand):
    args = '<>'
    help = 'List ClockPunches'
    scoreboard = {}
    work_periods = defaultdict(list)

    def post_activity_change(self, punch):
      duration = punch.timestamp - self.scoreboard[punch.worker]['start']
      self.work_periods[self.scoreboard[punch.worker]["job"]].append((punch.worker,duration))

    def close_all_sessions(self, timestamp):
      for worker in self.scoreboard.keys():
        duration = timestamp - self.scoreboard[worker]['start']
        self.work_periods[self.scoreboard[worker]['job']].append((worker, duration))
        del self.scoreboard[worker]

    def handle(self, *args, **options):

      break_event = Activity.objects.get(ticket="Break")
      open_event = Activity.objects.get(ticket="Open Shop")
      close_event = Activity.objects.get(ticket="Close Shop")

      dates = ClockPunch.objects.dates('timestamp','day')
      print break_event.pk
      punches = ClockPunch.objects.all().order_by('timestamp')
      print punches.count()
      for punch in punches:
        if punch.activity == open_event:
          pass
        elif punch.activity == close_event:
          self.close_all_sessions(punch.timestamp)
        elif punch.activity == break_event:
          if punch.worker not in self.scoreboard:
            pass
          else:
            self.post_activity_change(punch)
            del self.scoreboard[punch.worker]
        elif punch.worker not in self.scoreboard:
          self.scoreboard[punch.worker] = {"start" : punch.timestamp, 'job' : punch.activity}
        else:
          self.post_activity_change(punch)
          self.scoreboard[punch.worker] = {"start" : punch.timestamp, 'job' : punch.activity}

      summary_file = open('summary.csv', 'wb' )
      summary_report = csv.writer(summary_file)
      for job, work_sessions in self.work_periods.iteritems():
        session_total = datetime.timedelta(0)
        for session in work_sessions:
          session_total = session_total + session[1]
        session_total_seconds = (session_total.days * 24 * 60 * 60) + session_total.seconds
        hours,remainder = divmod(session_total_seconds,3600)
        minutes, seconds = divmod(remainder, 60)
        job_time = "%2d:%02d" % (hours, minutes)
        summary_report.writerow([job.ticket, job.description, job.job_complete, job_time])

#         if job.job_complete:
#           done = 'Complete'
#         else:
#           done = ''
#         print "%s - %s - %s" % (job.ticket, job.description, done)
#         session_total = datetime.timedelta(0)
#         for session in work_sessions:
#           print "\t %s \t %s" % (':'.join(str(session[1]).split(':')[:2]), session[0])
#           session_total = session_total + session[1]
#         print "Total: %s" % ':'.join(str(session_total).split(":")[:2])

# ':'.join(str(td).split(':')[:2])
#       for job, work_session in self.work_periods.iteritems():
#         self.stdout.write("%s - %s \n" % (job, [str(duration) for duration in self.work_periods[job] ]) )

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