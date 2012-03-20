from timeclock.models import ClockPunch, Worker, Activity
from django.contrib import admin


class ActivityAdmin(admin.ModelAdmin):
    #date_hierarchy = '<#...#>'
    list_display = ('ticket', 'description', 'on_work_queue', 'job_complete')
    list_editable = ('on_work_queue', 'job_complete') 
    list_filter = ('on_work_queue', 'job_complete') 
    #save_as = True
    save_on_top = True
    #inlines = [<#...#>]
 
 
admin.site.register(ClockPunch)
admin.site.register(Worker)
admin.site.register(Activity, ActivityAdmin)
