from .import views
from django.urls import path, include
from django.views.generic import ListView, DetailView
from .models import Notes


urlpatterns = [
    path('', views.index, name = 'main'),
    path('', ListView.as_view(queryset=Notes.objects.all().order_by('-created_on')[:5], template_name="/LibSite/notes.html"), name='Список новостей'),
    path('notes/<int:pk>', DetailView.as_view(model = Notes, template_name='LibSite/NewsPage.html'), name="News"),
    path('story', views.story, name = 'story'),
    path('newspage', views.newspage, name = 'news'),
    path('dostup', views.dostup, name = 'dostup'),
    path('tidings', views.tidings, name = 'tidings'), 
    path('oop', views.oop, name = 'oop'),
    path('services', views.services, name = 'services'),
    path('toktom', views.toktom, name = 'toktom'),
    path('new_books', views.nbook, name = 'nbooks'),
    path('info', views.info, name = 'info'),
    path('ek-instruction', views.instr1, name = 'instr1'),
    path('vkr-instruction', views.instr2, name = 'instr2'),
    path('e-library', views.elib, name = 'elib'),
    path('science_resurses', views.science_r, name = 'science_resurses'),
    path('science_naukometria', views.naukometria, name = 'science_naukometria'),
    path('library-discription', views.l_discription, name = 'library-discription'),
    path('reyting-statey', views.reyting, name = 'reyting'),
    path('vid-el-cat', views.vid_el_cat, name = 'vid-el-cat'),
    path('inf-res', views.inf_res, name = 'inf-res'),
    path('of_sci', views.of_sci, name = 'of-sci'),
    path('vyp_work', views.vyp_work, name = 'vyp-work'),
    path('education-portal-kyrlibnet', views.ed_kyrlibnet, name = 'ed-kyrlibnet'),
    path('ebs-university-library-online', views.ebs_ulo, name = 'ebs-ulo'),
    path('ebs-ulo-period', views.ulo_period, name = 'ebs-ulo-period'),
    path('reading-room', views.reading_room, name = 'reading-room'),
    path('registration-of-a-students-scientific-work', views.ss_work, name = 'ss-work'),
    path('Libraries-of-the-world', views.libsOftheWorld, name = 'libsOftheWorld'),
    path('our-partners', views.OurPartners, name = 'our-partners'),
    path('service-department', views.ServiceDepartment, name='service-department'),
    path('department-of-training-and-automation', views.DTA, name='DofTandA'),
    path('Department-of-eDocumentation-and-Bibliography', views.DofEDandB, name = 'DEDB'),
    path('dep-of-eCatalog-and-dev-of-information-resources', views.DofECandDevofIR, name = 'DECDIR'),
    path('fun-facts-about-libraries', views.IntFacts, name = 'IntFacts'),
    path('acquisition', views.acquisition, name = 'acquisition'),
] 