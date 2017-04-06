from __future__ import unicode_literals

from django.db import models
from Registration.models import *
# Create your models here.

# class AcademicyearClassRelation(models.Model):
#     class_id= models.ManyToManyField(ClassDetails)
#     academic_year = models.ForeignKey(AcademicYear, models.DO_NOTHING, blank=True, null=True)
# 
#     class Meta:
#         managed = False
#         db_table = 'academicyear_class_relation'
#         
        
# class AcademicyearClassRelation(models.Model):
#     class_id= models.ManyToManyField(ClassDetails)
#     academic_year = models.IntegerField(blank=True, null=True)
# 
#     class Meta:
#         managed = False
#         db_table = 'academicyear_class_relation'


class AcademicyearClassRelation(models.Model):
    class_id= models.ManyToManyField(ClassDetails)  # Field renamed because it was a Python reserved word.
    academic_year = models.ForeignKey(AcademicYear, models.DO_NOTHING, db_column='academic_year', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'academicyear_class_relation'
       


class AcademicyearClassRelationClassId(models.Model):
    academicyearclassrelation_id = models.IntegerField(blank=True, null=True)
    classdetails_id = models.IntegerField(blank=True, null=True)

    class Meta:
        
        managed = False
        db_table = 'academicyear_class_relation_class_id'
        

class ClassSectionMapping(models.Model):
    class_name = models.ForeignKey(ClassDetails, models.DO_NOTHING, db_column='class_name', blank=True, null=True)
    section_name = models.ManyToManyField(Sections)

    class Meta:
        managed = False
        db_table = 'class_section_mapping'


class ClassSectionMappingSectionName(models.Model):
    classsectionmapping_id = models.IntegerField(blank=True, null=True)
    sections_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'class_section_mapping_section_name'

class ClassTeacherMapping(models.Model):
    class_name = models.ForeignKey(ClassDetails, models.DO_NOTHING, db_column='class_name', blank=True, null=True)
    teacher_name = models.ManyToManyField(StaffDetails)

    class Meta:
        managed = False
        db_table = 'class_teacher_mapping'

class ClassTeacherMappingTeacherName(models.Model):
    classteachermapping_id = models.IntegerField(blank=True, null=True)
    staffdetails_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'class_teacher_mapping_teacher_name'
        


class ClassSubjectMapping(models.Model):
    class_name = models.ForeignKey(ClassDetails, models.DO_NOTHING, db_column='class_name', blank=True, null=True)
    subject_name =  models.ManyToManyField(Subject)

    class Meta:
        managed = False
        db_table = 'class_subject_mapping'
        
        
class ClassSubjectMappingSubjectName(models.Model):
    classsubjectmapping_id = models.IntegerField(blank=True, null=True)
    subject_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'class_subject_mapping_subject_name'
        
class RoleUserRelation(models.Model):
    role_name = models.ForeignKey(Role, models.DO_NOTHING, db_column='role_name', blank=True, null=True)
    user_name = models.ManyToManyField(StaffDetails)
    class Meta:
        managed = False
        db_table = 'role_user_relation'
        
class RoleUserRelationUserName(models.Model):
    roleuserrelation_id = models.IntegerField(blank=True, null=True)
    staffdetails_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'role_user_relation_user_name'
        
class TeacherSubjectRelation(models.Model):
    
    teacher_name = models.ForeignKey(StaffDetails, models.DO_NOTHING, db_column='teacher_name', blank=True, null=True)
    subject_name = models.ManyToManyField(Subject)
    class Meta:
        managed = False
        db_table = 'teacher_subject_relation'



class TeacherSubjectRelationSubjectName(models.Model):
    teachersubjectrelation_id = models.IntegerField(blank=True, null=True)
    subject_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'teacher_subject_relation_subject_name'




class SupervisorClassRelation(models.Model):
    supervisor_name = models.ForeignKey(StaffDetails, models.DO_NOTHING, db_column='supervisor_name', blank=True, null=True)
    class_name =  models.ManyToManyField(ClassDetails)
    class Meta:
        managed = False
        db_table = 'supervisor_class_relation'

class SupervisorClassRelationClassName(models.Model):
    supervisorclassrelation_id = models.IntegerField(blank=True, null=True)
    classdetails_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'supervisor_class_relation_class_name'




class StudentOptionalSubjectMapping(models.Model):
    student_name = models.ManyToManyField(StudentDetails) 
    subject_name = models.ManyToManyField(Subject) 

    class Meta:
        managed = False
        db_table = 'student_optional_subject_mapping'


        
class StudentOptionalSubjectMappingStudentName(models.Model):
    studentoptionalsubjectmapping_id = models.IntegerField(blank=True, null=True)
    studentdetails_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'student_optional_subject_mapping_student_name'


class StudentOptionalSubjectMappingSubjectName(models.Model):
    studentoptionalsubjectmapping_id = models.IntegerField(blank=True, null=True)
    subject_id = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'student_optional_subject_mapping_subject_name'


