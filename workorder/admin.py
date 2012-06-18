from django.contrib import admin

from workorder.models import Customer, WorkOrder, WorkOrderItem

admin.site.register(Customer)

class WorkOrderItemInline(admin.StackedInline):
    model = WorkOrderItem
    extras = 1

class WorkOrderAdmin(admin.ModelAdmin):
    inlines = [ WorkOrderItemInline, ]

admin.site.register(WorkOrder, WorkOrderAdmin)