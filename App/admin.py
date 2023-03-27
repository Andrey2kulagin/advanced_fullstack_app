from django.contrib import admin
from .models import Candidate


class CandidateAdmin(admin.ModelAdmin):
    list_display = [
        "first_name",
        "last_name",
        "email",
        'job',
        'age',
        'phone_number',
        'situation',
        'created_at'

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
    


admin.site.register(Candidate, CandidateAdmin)
