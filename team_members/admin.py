from team_members.apps import TeamMembersConfig
from django.contrib import admin

from .models import Team


class TeamAdmin(admin.ModelAdmin):
  list_display = ('id', 'name', 'email', 'join_date')
  list_display_links = ('id', 'name')
  search_fields = ('name',)
  list_per_page = 25


admin.site.register(Team, TeamAdmin)
