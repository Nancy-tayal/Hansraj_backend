from django.contrib import admin
from .models import StudentDetail

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ('sid','email','name','university_roll_no','course','semester','get_subject')
    list_filter = ('sid',)
    search_fields = ('sid',)
    ordering = ('sid',)
    filter_horizontal = ()
    def get_subject(self, instance):
        return [subject for subject in instance.subject.all()]


# Now register the new StudentAdmin
admin.site.register(StudentDetail, StudentAdmin)
