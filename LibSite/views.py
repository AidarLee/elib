from django.shortcuts import render
from django.utils import timezone
from django.views.generic.base import View
from django.views.generic.list import ListView

# Create your views here.

from django.shortcuts import render
from .models import Category, Recruitment, Video, Comment, Notes
from django.http import HttpResponse


def index(request):
	notes = Notes.objects.all()
	template_name = 'news/notes.html',
	return render(request, template_name, {'notes': notes})

def newspage(request):
	notes = Notes.objects.all()
	template_name = 'LibSite/layout.html'
	return render(request, template_name, {'notes': notes})

def story(request):
	template_name = "LibSite/storypage.html"
	return render(request, template_name)

def dostup(request):
	template_name = "LibSite/dostup_db_stl_kstu.html"
	return render(request, template_name)

def tidings(request):
	template_name = "LibSite/tidings.html"
	return render(request, template_name)

def oop(request):
	template_name = "LibSite/oop.html"
	return render(request, template_name)

def services(request):
	template_name = "LibSite/services.html"
	return render(request, template_name)

def toktom(request):
	template_name = "LibSite/toktom.html"
	return render(request, template_name)

def nbook(request):
	template_name = "LibSite/new_books.html"
	return render(request, template_name)

def info(request):
	template_name = "LibSite/info.html"
	return render(request, template_name)

def instr1(request):
	template_name = "LibSite/instr1.html"
	return render(request, template_name)

def instr2(request):
	template_name = "LibSite/instr2.html"
	return render(request, template_name)

def elib(request):
	template_name = "LibSite/elib.html"
	return render(request, template_name)

def science_r(request):
	template_name = "LibSite/science_resurses.html"
	return render(request, template_name)

def naukometria(request):
	template_name = "LibSite/science_naukometria.html"
	return render(request, template_name)

def l_discription(request):
	template_name = "LibSite/library-discription.html"
	return render(request, template_name)

def reyting(request):
	template_name = "LibSite/reyting_statey.html"
	return render(request, template_name)

def vid_el_cat(request):
	template_name = "LibSite/vid-el-cat.html"
	return render(request, template_name)

def inf_res(request):
	template_name = "LibSite/ins-res.html"
	return render(request, template_name)

def of_sci(request):
	template_name = "LibSite/of-sci-work-stud.html"
	return render(request, template_name)

def vyp_work(request):
	template_name = "LibSite/vyp-work.html"
	return render(request, template_name)

def ed_kyrlibnet(request):
	template_name = "LibSite/education-kyrlibnet.html"
	return render(request, template_name)

def ebs_ulo(request):
	template_name = "LibSite/ebs-ulo.html"
	return render(request, template_name)

def ulo_period(request):
	template_name = "LibSite/ulo-period.html"
	return render(request, template_name)

def reading_room(request):
	template_name = "LibSite/reading-room.html"
	return render(request, template_name)

def ss_work(request):
	template_name = "LibSite/students-science-work.html"
	return render(request, template_name)

def libsOftheWorld(request):
	template_name = "LibSite/libraries-of-th-world.html"
	return render(request, template_name)

def OurPartners(request):
	template_name = "LibSite/our-partners.html"
	return render(request, template_name)

def ServiceDepartment(request):
	template_name = "LibSite/service-department.html"
	return render(request, template_name)

def DTA(request):
	template_name = "LibSite/Department-of-Training-and-Automation.html"
	return render(request, template_name)

def DofEDandB(request):
	template_name = "LibSite/Dep-of-EDoc-and-Bibliography.html"
	return render(request, template_name)

def DofECandDevofIR(request):
	template_name = "LibSite/Dep-of-eCatalog-and-Dev-of-IR.html"
	return render(request, template_name)

def IntFacts(request):
	template_name = "LibSite/interesting-facts.html"
	return render(request, template_name)

def acquisition(request):
	template_name = "LibSite/acquisition.html"
	return render(request, template_name)

