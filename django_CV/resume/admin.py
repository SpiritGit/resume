from django.contrib import admin
from .models import Profile, Work, Skill, Edu, EProfile, EWork, ESkill, EEdu, AcaOutput, PracOutput, CSoutput, ECSoutput
# Register your models here.
admin.site.register(Profile)
admin.site.register(Work)
admin.site.register(Skill)
admin.site.register(Edu)
admin.site.register(EProfile)
admin.site.register(EWork)
admin.site.register(ESkill)
admin.site.register(EEdu)
admin.site.register(AcaOutput)
admin.site.register(PracOutput)
admin.site.register(CSoutput)
admin.site.register(ECSoutput)