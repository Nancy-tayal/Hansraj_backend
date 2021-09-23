from django.contrib import admin
from .models import FacultyDetail, SubjectDetail

# Register your models here.
class FacultyAdmin(admin.ModelAdmin):
    list_display = ('tid','email','name','department',)
    list_filter = ('tid',)
    search_fields = ('tid',)
    ordering = ('tid',)
    filter_horizontal = ()

class SubjectAdmin(admin.ModelAdmin):
    list_display = ('tid','subject_id','subject_name',)
    list_filter = ('subject_id',)
    search_fields = ('subject_id',)
    ordering = ('subject_id',)
    filter_horizontal = ()

# Now register the new StudentAdmin...
admin.site.register(FacultyDetail, FacultyAdmin)
admin.site.register(SubjectDetail, SubjectAdmin)

