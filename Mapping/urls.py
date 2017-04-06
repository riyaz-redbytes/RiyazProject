from django.conf.urls import include, url
from django.contrib import admin
from . import views
from django.contrib.auth.views import logout
from django.conf import settings
from django.conf.urls.static import static

app_name = 'Mapping'


urlpatterns = [
    ######################  ACADEMIC YEAR & CLASS MAPPING URLS ##############################
    url(r'^classAcedemicyear/$', views.ClassAcedemicyear, name='classAcedemicyear'),
     url(r'^academicyearClassMapping/$', views.AcademicyearClassMapping, name='academicyearClassMapping'),
     url(r'^viewMultisectClassList/$',views.ViewMultisectClassList, name='viewMultisectClassList'),
     url(r'^class_academic_mapping/$', views.ClassAcedemicMapping, name='class_academic_mapping'),
    
     
    ######################  Class Section MAPPING URLS #######################################
        url(r'^sectionClass/$', views.SectionClass, name='sectionClass'),
        url(r'^classSectionMapping/$', views.ClassSectionMaping, name='classSectionMapping'),
        url(r'^viewMultisectSectionList/$',views.ViewMultisectSectionList, name='viewMultisectSectionList'),

        ###################### Class Teacher Mapping URLS ##########################################
        url(r'^teacherClass/$', views.TeacherClass, name='teacherClass'),
        url(r'^classTeacherMapping/$', views.ClassTeacherMaping, name='classTeacherMapping'),
        url(r'^viewMultisectTeacherList/$',views.ViewMultisectTeacherList, name='viewMultisectTeacherList'),
        
    ######################  Class Subject MAPPING URLS ##############################
        url(r'^subjectClass/$', views.ClassSubject, name='subjectClass'),
        url(r'^classSubjectMapping/$', views.ClassSubjectMaping, name='classSubjectMapping'),
        url(r'^viewMultisectSubjectList/$',views.ViewMultisectSubjectList, name='viewMultisectSubjectList'),
        
     ######################  Role User MAPPING URLS ########################################
        url(r'^roleUser/$', views.RoleUser, name='roleUser'),
        url(r'^roleUserMapping/$', views.RoleUserMapping, name='roleUserMapping'),
        url(r'^viewMultiselectUserList/$',views.ViewMultiselectUserList, name='viewMultiselectUserList'),
        
      ######################  Teacher Subject MAPPING URLS ########################################
        url(r'^teacherSubject/$', views.TeacherSubject, name='teacherSubject'),
        url(r'^teacherSubjectMapping/$', views.TeacherSubjectMapping, name='teacherSubjectMapping'),
        url(r'^viewSectionDetails/$',views.ViewSectionDetail, name='viewSectionDetails'),
        url(r'^viewMultiselectTeacherSubjectList/$',views.ViewMultiselectTeacherSubjectList, name='viewMultiselectTeacherSubjectList'),
       ###################### SUPERVISOR CLASS MAPPING URLS ########################################
        url(r'^supervisorClass/$', views.SupervisorClass, name='supervisorClass'),
        url(r'^supervisorClassMapping/$', views.SupervisorClassMapping, name='supervisorClassMapping'),
        url(r'^viewMultiselectSupervisorClassList/$',views.ViewMultiselectSupervisorClassList, name='viewMultiselectSupervisorClassList'),


    
       ######################  Student optional Subject MAPPING URLS ########################################
         url(r'^studentSubject/$', views.StudentSubject, name='studentSubject'),
         url(r'^studentSubjectMapping/$', views.StudentSubjectMapping, name='studentSubjectMapping'),
         url(r'^viewSectionDetail/$',views.ViewSectionDetails, name='viewSectionDetail'),
         url(r'^viewFilteredStudent/$',views.ViewFilteredStudent, name='viewFilteredStudent'),
 
   
   ]
