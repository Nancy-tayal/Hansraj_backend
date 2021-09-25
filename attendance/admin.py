from django.contrib import admin
from .models import Attendance, Attendance_Out_Of
# Register your models here.
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('sid', 'detail_id', 'm1', 'm2', 'm3', 'm4', 'm5', 'm6', 'm7', 'm8', 'm9', 'm10', 'm11', 'm12', 'total')
    list_filter = ('sid','detail_id')
    search_fields = ('sid','detail_id')
    ordering = ('sid',)
    filter_horizontal = ()

admin.site.register(Attendance, AttendanceAdmin)

class Attendance_Out_Of_Admin(admin.ModelAdmin):
    list_display = ('detail_id', 'm1', 'm2', 'm3', 'm4', 'm5', 'm6', 'm7', 'm8', 'm9', 'm10', 'm11', 'm12', 'total')
    list_filter = ('detail_id',)
    search_fields = ('detail_id',)
    ordering = ('detail_id',)
    filter_horizontal = ()

admin.site.register(Attendance_Out_Of, Attendance_Out_Of_Admin)

