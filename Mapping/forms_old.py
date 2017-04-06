
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
    teacher_name = forms.ModelChoiceField(queryset= StaffDetail,widget=forms.Select(attrs={'class':'form-control' , 'autocomplete': 'off'}))
   
    subject_name = forms.ModelMultipleChoiceField(queryset=Subject.objects.all(), widget=FilteredSelectMultiple("Subject", is_stacked=False))
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
        
       
    