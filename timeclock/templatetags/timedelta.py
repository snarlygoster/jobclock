from django import template

register = template.Library()

@register.filter
def timedelta_fmt(td):
  secs = td.seconds + td.days * 24 * 3600
  return "%d:%02d" % (secs/3600, secs%3600/60)
