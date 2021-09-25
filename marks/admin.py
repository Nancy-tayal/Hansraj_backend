from django.contrib import admin
from .models import Marks, Marks_Out_Of
# Register your models here.
class MarksAdmin(admin.ModelAdmin):
    list_display = ('sid', 'detail_id', 'a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'a9', 'a10', 'i1', 'i2', 'i3', 'practical', 'total')
    list_filter = ('sid','detail_id')
    search_fields = ('sid','detail_id')
    ordering = ('sid',)
    filter_horizontal = ()

admin.site.register(Marks, MarksAdmin)

class Marks_Out_Of_Admin(admin.ModelAdmin):
    list_display = ('detail_id', 'a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'a9', 'a10', 'i1', 'i2', 'i3', 'practical', 'total')
    list_filter = ('detail_id',)
    search_fields = ('detail_id',)
    ordering = ('detail_id',)
    filter_horizontal = ()

admin.site.register(Marks_Out_Of, Marks_Out_Of_Admin)

