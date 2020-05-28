from django.shortcuts import render
from .models import Profile, Work, Skill, Edu, EProfile, EWork, ESkill, EEdu, AcaOutput, PracOutput, CSoutput, ECSoutput
# Create your views here.
def home(request):
    Profiles = EProfile.objects.all().first()
    Works = EWork.objects.all()
    Skills = ESkill.objects.all()
    Edus = EEdu.objects.all()
    AcademicOutputs = AcaOutput.objects.all()
    Projects = ECSoutput.objects.all()
    return render(request,'resume/home.html',{'profile':Profiles,'works':Works,'skills':Skills,'edus':Edus,'acaout':AcademicOutputs,'projects':Projects})

def chome(request):
    Profiles = Profile.objects.all().first()
    Works = Work.objects.all()
    Skills = Skill.objects.all()
    Edus = Edu.objects.all()
    AcademicOutputs = AcaOutput.objects.all()
    Projects = CSoutput.objects.all()
    return render(request,'resume/chome.html',{'profile':Profiles,'works':Works,'skills':Skills,'edus':Edus,'acaout':AcademicOutputs,'projects':Projects})

