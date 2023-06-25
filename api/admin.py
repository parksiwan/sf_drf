from django.contrib import admin
from .models import SFTask, SFOutward, SFInward
from import_export.admin import ImportExportModelAdmin

# Register your models here.
#admin.site.register(SFTask)
#admin.site.register(SFOutward)
#admin.site.register(SFInward)

@admin.register(SFInward)
class ViewAdmin(ImportExportModelAdmin):
    list_display = ['eta_date_only', 'supplier', 'products', 'person_ordered', 'created_date', 'person_received', 'received_date', 'product_owner', 'location']
    search_fields = ['supplier', 'products', 'product_owner']
    filter_horizontal = ()
    date_hierarchy = 'eta'
    fieldsets = ()

    def eta_date_only(self, obj):
        return obj.eta.strftime("%d %b %Y")
    eta_date_only.admin_order_field = 'eta'
    eta_date_only.short_description = 'eta date' 


@admin.register(SFOutward)
class ViewAdmin(ImportExportModelAdmin):
    list_display = ['etd_date_only', 'customer', 'product_type', 'pallet_space', 'freight_company', 'created_date', 'person_booked', 'dispatched_date', 'person_dispatched']
    search_fields = ['customer', 'freight_company']
    filter_horizontal = ()
    date_hierarchy = 'etd'
    fieldsets = ()

    def etd_date_only(self, obj):
        return obj.etd.strftime("%d %b %Y")
    etd_date_only.admin_order_field = 'etd'
    etd_date_only.short_description = 'etd date'


@admin.register(SFTask)
class ViewAdmin(ImportExportModelAdmin):
    list_display = ['due_date_only', 'title', 'contents', 'created_date', 'creator', 'priority', 'assignee', 'completed_date']
    search_fields = ['title', 'contents']
    filter_horizontal = ()
    date_hierarchy = 'due_date'
    fieldsets = ()

    def due_date_only(self, obj):
        return obj.due_date.strftime("%d %b %Y")
    due_date_only.admin_order_field = 'due_date'
    due_date_only.short_description = 'due date'

