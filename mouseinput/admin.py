from django.contrib import admin
from .models import MouseEvent
import csv
from django.http import HttpResponse

# admin.site.register(MouseEvent)

def export_as_csv(modeladmin, request, queryset):
    meta = modeladmin.model._meta
    field_names = [field.name for field in meta.fields]

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
    writer = csv.writer(response)

    writer.writerow(field_names)
    for obj in queryset:
        row = writer.writerow([getattr(obj, field) for field in field_names])

    return response

export_as_csv.short_description = "Selected items to CSV"

@admin.register(MouseEvent)
class MouseEventAdmin(admin.ModelAdmin):
    list_display = ['event_type', 'x', 'y', 'timestamp']
    actions = [export_as_csv]