from django.contrib import admin
from .models import Candidate,Voter,VoterDetails


@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    list_display = ('candidate_name','candidate_info','vote_count')
admin.site.register(VoterDetails)
admin.site.site_header = 'Voting System Administration'
admin.site.site_header = 'Voting System Administration'