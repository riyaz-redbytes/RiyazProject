
from django import forms
import itertools
from Mapping.models import *
from Registration.models import *
from django.contrib.admin.widgets import FilteredSelectMultiple


class AcademicyearClassRelationForm(forms.ModelForm):
    AcademicYear = AcademicYear.objects.all()
    class_id = forms.ModelMultipleChoiceField(queryset=ClassDetails.objects.all(), widget=FilteredSelectMultiple("ClassDetails", is_stacked=False))
    academic_year = forms.ModelChoiceField(queryset = AcademicYear ,widget=forms.Select(attrs={'class':'form-control' , 'autocomplete': 'off'}))

    class Meta:
        model =AcademicyearClassRelation
        fields = ['class_id','academic_year']
 
 
 
class ClassSectionRelationForm(forms.ModelForm):
    ClassDetail = ClassDetails.objects.all()
    class_name = forms.ModelChoiceField(queryset = ClassDetail ,widget=forms.Select(attrs={'class':'form-control' , 'autocomplete': 'off'}))
 
    section_name = forms.ModelMultipleChoiceField(queryset=Sections.objects.all(), widget=FilteredSelectMultiple("Sections", is_stacked=False))
    class Meta:
        model = ClassSectionMapping
        fields = ['class_name','section_name']
        
        
 
class ClassSubjectMappingForm(forms.ModelForm):
    ClassDetail = ClassDetails.objects.all()
    class_name = forms.ModelChoiceField(queryset = ClassDetail ,widget=forms.Select(attrs={'class':'form-control' , 'autocomplete': 'off'}))
 
    subject_name = forms.ModelMultipleChoiceField(queryset=Subject.objects.all(), widget=FilteredSelectMultiple("Subject", is_stacked=False))
    class Meta:
        model = ClassSubjectMapping
        fields = ['class_name','subject_name']
    def __init__(self, *args, **kwargs):
        
         super(ClassSubjectMappingForm, self).__init__(*args, **kwargs)
         finalDict1=[]
         queryset1 = Subject.objects.filter(type = "Mandatory")
         finalDict1.append(list(itertools.chain(queryset1)))
         cnt=0
         k=[]
         for r in finalDict1:
            if len(r)!=0:
             for s in r:
                 print (s)
                 k.append(s)
         self.fields['subject_name'].queryset = Subject.objects.filter(id__in=[r.id for r in k])
        
class RoleUserRelationForm(forms.ModelForm):
    RoleDetail = Role.objects.all()
    user_name = forms.ModelMultipleChoiceField(queryset=StaffDetails.objects.all(), widget=FilteredSelectMultiple("StaffDetails", is_stacked=False))
    role_name = forms.ModelChoiceField(queryset = RoleDetail ,widget=forms.Select(attrs={'class':'form-control' , 'autocomplete': 'off'}))
    class Meta:
        model = RoleUserRelation
        fields = ['user_name','role_name']
        
     
    def __init__(self, *args, **kwargs):
        
         super(RoleUserRelationForm, self).__init__(*args, **kwargs)
         finalDict1=[]
         queryset1 = StaffDetails.objects.filter(role_type__isnull=True)
         finalDict1.append(list(itertools.chain(queryset1)))
         cnt=0
         k=[]
         for r in finalDict1:
            if len(r)!=0:
             for s in r:
                 print (s)
                 k.append(s)
         self.fields['user_name'].queryset = StaffDetails.objects.filter(id__in=[r.id for r in k])
        
class TeacherSubjectRelationForm(forms.ModelForm):
   
    StaffDetail = StaffDetails.objects.filter(role_type = 2)   
    #teacher_name = forms.ModelChoiceField(queryset= StaffDetail,widget=forms.Select(attrs={'class':'form-control' , 'autocomplete': 'off'}))
    teacher_name = forms.ModelMultipleChoiceField(queryset=StaffDetail, widget=forms.SelectMultiple(attrs={'class':'form-control' , 'autocomplete': 'off'}))
    subject_name = forms.ModelMultipleChoiceField(queryset=Subject.objects.all(), widget=FilteredSelectMultiple("Subject", is_stacked=False))
    assistant_teacher = forms.ModelMultipleChoiceField(queryset=StaffDetails.objects.filter(role_type=15), widget=forms.SelectMultiple(attrs={'class':'form-control' , 'autocomplete': 'off'}))
    class_name = forms.ModelMultipleChoiceField(queryset=ClassDetails.objects.all(), widget=forms.SelectMultiple(attrs={'class':'form-control' , 'autocomplete': 'off'}))
    section_name = forms.ModelMultipleChoiceField(queryset=Sections.objects.none(), widget=forms.SelectMultiple(attrs={'class':'form-control' , 'autocomplete': 'off'}))
    
    class Meta:
        model = TeacherSubjectRelation
        fields = ['subject_name','teacher_name']
        
 
class SupervisorClassRelationForm(forms.ModelForm):
    StaffDetail = StaffDetails.objects.filter(role_type = 3)  
    supervisor_name = forms.ModelChoiceField(queryset = StaffDetail ,widget=forms.Select(attrs={'class':'form-control' , 'autocomplete': 'off'}))
 
    class_name = forms.ModelMultipleChoiceField(queryset=ClassDetails.objects.all(), widget=FilteredSelectMultiple("ClassDetail", is_stacked=False))
    class Meta:
        model = SupervisorClassRelation
        fields = ['supervisor_name','class_name']
        
class ClassTeacherRelationForm(forms.ModelForm):
    ClassDetail = ClassDetails.objects.all()
    class_name = forms.ModelChoiceField(queryset = ClassDetail ,widget=forms.Select(attrs={'class':'form-control' , 'autocomplete': 'off'}))
    teacher_name = forms.ModelMultipleChoiceField(queryset=StaffDetails.objects.filter(role_type=2), widget=FilteredSelectMultiple("Sections", is_stacked=False))
    
    class Meta:
        model = ClassTeacherMapping
        fields = ['class_name','teacher_name']      


class StudentOptionalSubjectMappingForm(forms.ModelForm):
    SectionDetail = Sections.objects.all()
    ReligionDetail = Religion.objects.all()
    NationalityDetail = Nationality.objects.all()
    ClassDetail = ClassDetails.objects.all()
    religion = forms.ModelMultipleChoiceField(required=False ,queryset = ReligionDetail ,widget=forms.SelectMultiple(attrs={'class':'form-control' , 'autocomplete': 'off'}))
    nationality = forms.ModelMultipleChoiceField(required=False ,queryset = NationalityDetail ,widget=forms.SelectMultiple(attrs={'class':'form-control' , 'autocomplete': 'off'}))
  
    class_name = forms.ModelMultipleChoiceField(required=False , queryset = ClassDetail ,widget=forms.SelectMultiple(attrs={'class':'form-control' , 'autocomplete': 'off'}))
    section_name = forms.ModelMultipleChoiceField(required=False ,queryset = SectionDetail ,widget=forms.SelectMultiple(attrs={'class':'form-control' , 'autocomplete': 'off'}))
  
    subject_name = forms.ModelMultipleChoiceField(queryset=Subject.objects.all(), widget=FilteredSelectMultiple("Subject", is_stacked=False))
 
    student_name = forms.ModelMultipleChoiceField(queryset=StudentDetails.objects.all(), widget=FilteredSelectMultiple("StudentDetails", is_stacked=False))
    class Meta:
        model = StudentOptionalSubjectMapping
        fields = ['subject_name','student_name']
        
    def __init__(self, *args, **kwargs):
        
         super(StudentOptionalSubjectMappingForm, self).__init__(*args, **kwargs)
         finalDict1=[]
         queryset1 = Subject.objects.filter(type = "Optional")
         finalDict1.append(list(itertools.chain(queryset1)))
         cnt=0
         k=[]
         for r in finalDict1:
            if len(r)!=0:
             for s in r:
                 print (s)
                 k.append(s)
         self.fields['subject_name'].queryset = Subject.objects.filter(id__in=[r.id for r in k])
              
    
    
