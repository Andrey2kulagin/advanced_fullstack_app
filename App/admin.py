from django.contrib import admin
from .models import Candidate
from django.utils.html import format_html


class CandidateAdmin(admin.ModelAdmin):
    list_filter = ['Situation']
    list_display = [
        "first_name",
        "last_name",
        "email",
        'job',
        'age',
        'phone_number',
        'situation',
        'created_at',
        'status',
        '_'


    ]
    search_fields = [
        "first_name",
        "last_name",
        "email",
    ]
    list_per_page = 10

    def _(self, obj):
        if obj.situation == 'Approved':
            return True
        elif obj.situation == 'Pending':
            return None
        else:
            return False

    _.boolean = True

    def status(self, obj):
        if obj.situation == 'Approved':
            color = "#28a745"
        elif obj.situation == 'Pending':
            color = "#fea95e"
        else:
            color = 'red'
        return format_html('<strong><p style="color = {};">{}</p></strong>'.format(color, obj))
    status.allow_tags=True
admin.site.register(Candidate, CandidateAdmin)
