from django.shortcuts import render,redirect
from Mapping.models import *
from Mapping import forms
from .forms import *
from django.contrib import messages
from django.forms.models import model_to_dict, inlineformset_factory
from django.http import JsonResponse
# Create your views here.

####################### AcedemicYear Class Mapping #####################

def ClassAcedemicMapping(request):    
#    studentList = StudentDetails.objects.all()
#     print 'studentList',studentList
#     print "in hme...gggg......"
    return render(request, "academic_mapping_view.html", {})
#

    ###########SHOWS ACADEMIC YEAR & CLASS MAPPING#############
def ClassAcedemicyear(request):
    AcademicyearClassRelation = AcademicyearClassRelationForm()
    return render(request,'academycyear_class_mapping.html', {'AcademicyearClassRelationForm':AcademicyearClassRelation})
    
    
    ##############Save ACADEMIC YEAR & CLASS MAPPING Form######
def AcademicyearClassMapping(request):
    print"in post1"
    if request.method == 'POST':
        print"in post"
        form = AcademicyearClassRelationForm(request.POST)
        if form.is_valid():
            form.save()
    return redirect('/school/classAcedemicyear/')
             
    ##############Save ACADEMIC YEAR & CLASS MAPPING Form######
def ViewMultisectClassList(request):
    print "in ViewMultisectClassList............"
    modelDict=[]
    academic_year = request.GET.get('academic_year',None)
    print ">>>>>>>>>>>>>", academic_year
    AcademicyearClassRel = AcademicyearClassRelation.objects.filter(academic_year = academic_year)
    for obj in AcademicyearClassRel:
        print" AcademicyearClassRelation.id",obj.id
        AcademicyearClassRel_Id = obj.id
        academicYearclass_obj = AcademicyearClassRelationClassId.objects.filter(academicyearclassrelation_id = AcademicyearClassRel_Id)
        print"academicYearclass_obj",academicYearclass_obj
        for object in academicYearclass_obj:
            classId = object.classdetails_id
            print "classId",classId
            ClassDetail = ClassDetails.objects.filter(id = classId) 
            for obj in ClassDetail:
                modelDict.append(model_to_dict(obj)) 
    return JsonResponse(modelDict,safe=False)

######################################AcedemicYear Class Mapping Ends#########################################



####################### Class Section Mapping #####################

    ###########SHOWS Class Section MAPPING#############
def SectionClass(request):
    print"in section class"
    ClassSectionRelation = ClassSectionRelationForm()
    return render(request,'class_section_mapping.html', {'ClassSectionRelationForm':ClassSectionRelation})
 ##############Save ACADEMIC YEAR & CLASS MAPPING Form######
def ClassSectionMaping(request):
    print"in post1"
    if request.method == 'POST':
        print"in post"
        form = ClassSectionRelationForm(request.POST)
        if form.is_valid():
            form.save()
    return redirect('/school/sectionClass/')     
     
def ViewMultisectSectionList(request):
    print "ViewMultisectSectionList............"
    print "in ViewMultisectClassList............"
    modelDict=[]
    class_name = request.GET.get('class_name',None)
    print ">>>>>>>>>>>>>", class_name
    ClassSectionMap = ClassSectionMapping.objects.filter(class_name = class_name)
    print"ClassSectionMap",ClassSectionMap
    for obj in ClassSectionMap:
        print" ClassSectionMapping",obj.id
        ClassSectionMapping_Id = obj.id
        ClassSectionMappingSectionName_obj = ClassSectionMappingSectionName.objects.filter(classsectionmapping_id  =  ClassSectionMapping_Id )
        print"ClassSectionMappingSectionName_obj ",ClassSectionMappingSectionName_obj 
        for object in ClassSectionMappingSectionName_obj :
            sectionsId = object.sections_id
            print "ssectionsId",sectionsId
            Section = Sections.objects.filter(id = sectionsId) 
            for obj in Section:
                modelDict.append(model_to_dict(obj)) 
    return JsonResponse(modelDict,safe=False)
      
     
####################### ClassSubject Mapping #####################

    ###########SHOWS ClassSubject MAPPING#############
def ClassSubject(request):
    print"in section class"
    ClassSubjectMapping = ClassSubjectMappingForm()
    return render(request,'class_subject_mapping.html', {'ClassSubjectMappingForm':ClassSubjectMapping})


##############Save Class Section MAPPING Form######
def ClassSubjectMaping(request):
    print"in post1"
    if request.method == 'POST':
        print"in post"
        form = ClassSubjectMappingForm(request.POST)
        if form.is_valid():
            form.save()
    return redirect('/school/subjectClass/')     

def ViewMultisectSubjectList(request):
    print "in ViewMultisectClassList............"
    modelDict=[]
    class_name1 = request.GET.get('class_name',None)
    print ">>>>>>>>>>>>>", class_name1
    ClassSubjectMaping = ClassSubjectMapping.objects.filter(class_name = class_name1)
    for obj in ClassSubjectMaping:
        print" ClassSubjectMaping",obj.id
        ClassSubjectMaping_Id = obj.id
        ClassSubjectMappingSubjectName_obj = ClassSubjectMappingSubjectName.objects.filter(classsubjectmapping_id  =  ClassSubjectMaping_Id )
        print"ClassSubjectMappingSubjectName_obj",ClassSubjectMappingSubjectName_obj
        for object in ClassSubjectMappingSubjectName_obj:
            subjectId = object.subject_id
            print "subjectId",subjectId
            subject = Subject.objects.filter(id = subjectId) 
            for obj in subject:
                modelDict.append(model_to_dict(obj)) 
    return JsonResponse(modelDict,safe=False)


####################### Class-Teacher Mapping ##################################

##########SHOWS Class Teacher MAPPING#############
def TeacherClass(request):
    print"in teacher class"
    ClassTeacherRelation = ClassTeacherRelationForm()
    return render(request,'class_teacher_mapping.html', {'ClassTeacherRelationForm':ClassTeacherRelation})

def ClassTeacherMaping(request):
    print"in post1"
    if request.method == 'POST':
        print"in post"
        form = ClassTeacherRelationForm(request.POST)
        if form.is_valid():
            form.save()
    return redirect('/school/teacherClass/')     
     
def ViewMultisectTeacherList(request):
    
    print "in ViewMultisectClassList............"
    modelDict=[]
    class_name = request.GET.get('class_name',None)
    print ">>>>>>>>>>>>>", class_name
    ClassTeacherMap = ClassTeacherMapping.objects.filter(class_name = class_name)
    print"ClassteacherMap1",ClassTeacherMap
    for obj in ClassTeacherMap:
        print" ClassteacherMap",obj.id
        ClassTeacherMapping_Id = obj.id
        ClassTeacherMappingTeacherName_obj = ClassTeacherMappingTeacherName.objects.filter(classteachermapping_id  =  ClassTeacherMapping_Id )
        print"ClassTeacherMappingTeacherName_obj ",ClassTeacherMappingTeacherName_obj 
        for object in ClassTeacherMappingTeacherName_obj :
            teacherId = object.staffdetails_id
            print "ssectionsId",teacherId
            teacher = StaffDetails.objects.filter(id = teacherId) 
            for obj in teacher:
                modelDict.append(model_to_dict(obj)) 
            print "Modeldict",modelDict
    return JsonResponse(modelDict,safe=False)
    
####################### ROLE USER Mapping #####################

    ###########SHOWS ROLE USER Mapping #############
def RoleUser(request):
    print"in section class"
    RoleUserRelation = RoleUserRelationForm()
    return render(request,'role_user_mapping.html', {'RoleUserRelationForm':RoleUserRelation})



    ##############Save Role User  MAPPING Form######
def RoleUserMapping(request):
    print"in post1"
    if request.method == 'POST':
        print"in post"
        form = RoleUserRelationForm(request.POST)
        role_name =   request.POST['role_name']
        print"role_namerole_namerole_namerole_name",role_name
        user = request.POST.getlist('user_name') 
        userlist=[x.encode('UTF8') for x in user]
        print "useruseruseruseruseruseruseruseruseruser",userlist
        for obj in userlist:
          staff_id=int(obj)
          print "staff_idstaff_idstaff_idstaff_id",staff_id
          StaffDetail = StaffDetails.objects.get(id  =  staff_id )
          StaffDetail.role_type = role_name
          StaffDetail.save()
          
        if form.is_valid():
            form.save()
        
    return redirect('/school/roleUser/')  


def ViewMultiselectUserList(request):   
    print "in ViewMultiselectUserList............"
    modelDict=[]
    role_name = request.GET.get('role_name',None)
    print ">>>>>>>>>>>>>", role_name
    RoleUserRelationObj = RoleUserRelation.objects.filter(role_name = role_name)
    for obj in RoleUserRelationObj:
        print" ClassSubjectMaping",obj.id
        RoleUserRelationObj_Id = obj.id
        RoleUserRelationUserName_obj = RoleUserRelationUserName.objects.filter(roleuserrelation_id  =  RoleUserRelationObj_Id )
        print" RoleUserRelationUserName_obj", RoleUserRelationUserName_obj
        for object in  RoleUserRelationUserName_obj:
            staffdetailsId = object.staffdetails_id
            print "staffdetailsId",staffdetailsId
            User = StaffDetails.objects.filter(id = staffdetailsId) 
            for obj in User:
                modelDict.append(model_to_dict(obj)) 
    return JsonResponse(modelDict,safe=False)
      
     
     
####################### TEACHER SUBJECT Mapping #####################

    ###########SHOWS  TEACHER SUBJECT Mapping #############
def TeacherSubject(request):
    print"in section class"
   
    TeacherSubjectRelation = TeacherSubjectRelationForm()
             
    return render(request,'teacher_subject_mapping.html', {'TeacherSubjectRelationForm':TeacherSubjectRelation})

  ##############Save Teacher Subject MAPPING Form######
def TeacherSubjectMapping(request):
    print"iTeacherSubjectMappingTeacherSubjectMappingTeacherSubjectMappingTeacherSubjectMappingTeacherSubjectMapping"
    if request.method == 'POST':
        print"in post"
        form = TeacherSubjectRelationForm(request.POST)
        print form.errors
        if form.is_valid():
            form.save()
            print"save done........"
            
    return redirect('/school/teacherSubject/')  

def ViewMultiselectTeacherSubjectList(request):   
    print "in ViewMultiselectUserList............"
    modelDict=[]
    teacher_name = request.GET.get('teacher_name',None)
    print ">>>>>>>>>>>>>", teacher_name
    TeacherSubjectRelationObj = TeacherSubjectRelation.objects.filter(teacher_name = teacher_name)
    for obj in  TeacherSubjectRelationObj:
       print"  TeacherSubjectRelationObjMaping",obj.id
       TeacherSubjectRelationObj_Id = obj.id
       TeacherSubjectRelationSubjectName_obj = TeacherSubjectRelationSubjectName.objects.filter(teachersubjectrelation_id  =  TeacherSubjectRelationObj_Id )
       print" RoleUserRelationUserName_obj",  TeacherSubjectRelationSubjectName_obj
       for object in   TeacherSubjectRelationSubjectName_obj:
            subjectId = object.subject_id
            print "subjectId",subjectId
            subject = Subject.objects.filter(id = subjectId) 
            for obj in subject:
                modelDict.append(model_to_dict(obj)) 
    return JsonResponse(modelDict,safe=False)
      
####################### SUPERVISOR CLASS Mapping #####################

    ###########SHOWS  SUPERVISOR CLASS Mapping #############
def SupervisorClass(request):
    print"in section class"
   
    SupervisorClassRelation = SupervisorClassRelationForm()
             
    return render(request,'supervisor_class_mapping.html', {'SupervisorClassRelationForm': SupervisorClassRelation})
     
##############Supervisor Class  MAPPING Form######
def SupervisorClassMapping(request):
    print"in post1"
    if request.method == 'POST':
        print"in post"
        form = SupervisorClassRelationForm(request.POST)
        if form.is_valid():
            form.save()
    return redirect('/school/supervisorClass/')     

def ViewMultiselectSupervisorClassList(request):   
    print "in ViewMultiselectUserList............"
    modelDict=[]
    supervisor_name = request.GET.get('supervisor_name',None)
    print ">>>>>>>>>>>>>", supervisor_name
    SupervisorClassRelationObj = SupervisorClassRelation.objects.filter(supervisor_name = supervisor_name)
    for obj in  SupervisorClassRelationObj:
       print"  SupervisorClassRelationObj",obj.id
       SupervisorClassRelationObj_Id = obj.id
       SupervisorClassRelationClassName_obj = SupervisorClassRelationClassName.objects.filter(supervisorclassrelation_id  =  SupervisorClassRelationObj_Id )
       print" SupervisorClassRelationClassName_obj",  SupervisorClassRelationClassName_obj
       for object in   SupervisorClassRelationClassName_obj:
            classdetailsId = object.classdetails_id
            print " classdetailsId", classdetailsId
            ClassDetail = ClassDetails.objects.filter(id =  classdetailsId) 
            for obj in ClassDetail:
                modelDict.append(model_to_dict(obj)) 
    return JsonResponse(modelDict,safe=False)

####################### STUDENT OPTIONAL SUBJECT Mapping #####################

    ###########SHOWS STUDENT OPTIONAL SUBJECT Mapping #############
def StudentSubject(request):
    print"in StudentSubject"
   
    StudentOptionalSubjectMapping = StudentOptionalSubjectMappingForm()
             
    return render(request,'student_optional_subject_mapping.html', {'StudentOptionalSubjectMappingForm': StudentOptionalSubjectMapping})
        
# 
    ###########SHOWS STUDENT OPTIONAL SUBJECT Mapping Form #############
def StudentSubjectMapping(request):   
    print"in post1"
    if request.method == 'POST':
        print"in post"
        form = StudentOptionalSubjectMappingForm(request.POST)
        if form.is_valid():
            form.save()
    return redirect('/school/studentSubject/')      


def ViewSectionDetails(request):  
    
    print "in view section detail"
    print "ViewMultisectSectionList............"
    print "in ViewMultisectClassList............"
    modelDict=[]
    class_name = request.GET.get('class_name',None)
    print ">>>>>>>>>>>>>", class_name
    ClassSectionMap = ClassSectionMapping.objects.filter(class_name = class_name)
    print"ClassSectionMap",ClassSectionMap
    for obj in ClassSectionMap:
        print" ClassSectionMapping",obj.id
        ClassSectionMapping_Id = obj.id
        ClassSectionMappingSectionName_obj = ClassSectionMappingSectionName.objects.filter(classsectionmapping_id  =  ClassSectionMapping_Id )
        print"ClassSectionMappingSectionName_obj ",ClassSectionMappingSectionName_obj 
        for object in ClassSectionMappingSectionName_obj :
            sectionsId = object.sections_id
            print "ssectionsId",sectionsId
            Section = Sections.objects.filter(id = sectionsId)
            print "section:",Section
            for obj in Section:
                modelDict.append(model_to_dict(obj)) 
            print "modelDictmodelDictmodelDictmodelDictmodelDictmodelDictmodelDict",modelDict
    return JsonResponse(modelDict,safe=False)


def ViewFilteredStudent(request): 
    modelDict=[]
    print "ViewFilteredStudentViewFilteredStudentViewFilteredStudent"
    class_name = request.GET.get('class_name',None)
    print "class_name",class_name
    section_name = request.GET.get('section_name',None)
    print "section_name",section_name
    religion = request.GET.get('religion',None)
    print "religion",religion
    StudentList = StudentDetails.objects.filter(class_name=class_name,section=section_name,religion = religion)
    print "StudentListStudentListStudentList",StudentList
    for obj in StudentList:
        print obj.first_name
        name = obj.first_name
        modelDict.append(name) 
    print"modelDictmodelDictmodelDictmodelDictdfgjkfghjkjdfghjdfghjdfgjh",modelDict
            
    return JsonResponse(modelDict,safe=False)
    
  
              
