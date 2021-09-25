from django.contrib import admin
from .models import Timetable
# Register your models here.
class TimetableAdmin(admin.ModelAdmin):
    list_display = ('course', 'semester', 'day', 't1', 't2', 't3', 't4', 't5', 't6', 't7', 't8')
    list_filter = ('course',)
    search_fields = ('course','semester', 'day')
    ordering = ('course',)
    filter_horizontal = ()

admin.site.register(Timetable, TimetableAdmin)

