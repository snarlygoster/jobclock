from django.core.management.base import BaseCommand, CommandError
from timeclock.models import ClockPunch

class Command(BaseCommand):
    args = '<>'
    help = 'List ClockPunches'

    def handle(self, *args, **options):
        for poll_id in args:
            try:
                poll = Poll.objects.get(pk=int(poll_id))
            except Poll.DoesNotExist:
                raise CommandError('Poll "%s" does not exist' % poll_id)

            poll.opened = False
            poll.save()

            self.stdout.write('Successfully closed poll "%s"\n' % poll_id)