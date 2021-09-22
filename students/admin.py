from django.contrib import admin
from .models import StudentDetails

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ('uid','email','name','university_roll_no','course','semester',)
    list_filter = ('uid',)
    search_fields = ('uid',)
    ordering = ('uid',)
    filter_horizontal = ()

# Now register the new StudentAdmin...
admin.site.register(StudentDetails, StudentAdmin)