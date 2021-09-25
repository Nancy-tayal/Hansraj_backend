from django.contrib import admin
from .models import FacultyDetail, SubjectDetail, Subject

# Register your models here.
class FacultyAdmin(admin.ModelAdmin):
    list_display = ('tid','email','name','department',)
    list_filter = ('tid',)
    search_fields = ('tid',)
    ordering = ('tid',)
    filter_horizontal = ()

class SubjectDetailAdmin(admin.ModelAdmin):
    list_display = ('detail_id','subject_id','tid',)
    list_filter = ('subject_id',)
    search_fields = ('subject_id',)
    ordering = ('subject_id',)
    filter_horizontal = ()

class SubjectAdmin(admin.ModelAdmin):
    list_display = ('subject_id','subject_name')
    list_filter = ('subject_name',)
    search_fields = ('subject_name',)
    ordering = ('subject_name',)
    filter_horizontal = ()

# Now register the new StudentAdmin...
admin.site.register(FacultyDetail, FacultyAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(SubjectDetail, SubjectDetailAdmin)