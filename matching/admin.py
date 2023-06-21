from django.contrib import admin
from matching.models import Consultant, Skill, Mission, Requirement, User #, Human_ressource, Ressource_manager, Commercial

class ObjetSkill(admin.ModelAdmin):
    list_display = ('id', 'description')

class ObjetConsultant(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone')

"""
class ObjetHuman_ressource(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone', 'password')

class ObjetRessource_manager(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone', 'password')

class ObjetCommercial(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone', 'password')
"""

class ObjetUser(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone', 'office', 'password', 'role')

class ObjetMission(admin.ModelAdmin):
    list_display = ('description', 'client', 'writer')#_commercial', 'writer_ressource_manager')

class ObjetRequirement(admin.ModelAdmin):
    list_display = ('mission', 'skill', 'level')


admin.site.register(Skill, ObjetSkill)
admin.site.register(Consultant, ObjetConsultant)
#admin.site.register(Human_ressource, ObjetHuman_ressource)
#admin.site.register(Ressource_manager, ObjetRessource_manager)
#admin.site.register(Commercial, ObjetCommercial)
admin.site.register(User, ObjetUser)
admin.site.register(Mission, ObjetMission)
admin.site.register(Requirement, ObjetRequirement)

