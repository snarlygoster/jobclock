from timeclock.models import ClockPunch, Worker, Activity, WorkPeriod
from django.contrib import admin

admin.site.register(ClockPunch)

class ActivityAdmin(admin.ModelAdmin):
    #date_hierarchy = '<#...#>'
    list_display = ('ticket', 'description', 'on_work_queue', 'job_complete')
    list_editable = ('on_work_queue', 'job_complete')
    list_filter = ('on_work_queue', 'job_complete')
    #save_as = True
    save_on_top = True
    #inlines = [<#...#>]

admin.site.register(Activity, ActivityAdmin)

class WorkerAdmin(admin.ModelAdmin):
    list_display = ('name', 'can_work')
    list_editable = ( 'can_work',)
    list_filter = ('can_work',)

    save_as = True
    save_on_top = True

admin.site.register(Worker, WorkerAdmin)

class WorkPeriodAdmin(admin.ModelAdmin):
    list_display = ('worker','start_time','duration','job')

admin.site.register(WorkPeriod, WorkPeriodAdmin)