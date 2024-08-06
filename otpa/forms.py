from django import forms
from .models import Student, FeeRecord, ExamCard
from django import forms
from django.contrib.auth.models import User
# forms.py

# forms.py
from django import forms
from .models import OTPRecord, Student, Exam
from .models import Exam

from .models import Student, Course, AttendanceRecord

class AttendanceForm(forms.ModelForm):
    class Meta:
        model = AttendanceRecord
        fields = ['student', 'course', 'is_present']
    
    student = forms.ModelChoiceField(queryset=Student.objects.all(), label='Student Name')
    course = forms.ModelChoiceField(queryset=Course.objects.all(), label='Course Name')
    is_present = forms.BooleanField(required=False, label='I am present')


from django import forms
from .models import AttendanceRecord, Student

class ConfirmAttendanceForm(forms.Form):
    student = forms.ModelChoiceField(
        queryset=Student.objects.none(),  # Initially empty; will be populated by view
        required=True,
        label="Select Student"
    )
    confirmed_by_lecturer = forms.BooleanField(
        required=False,
        label="Confirm Attendance"
    )

    def __init__(self, *args, **kwargs):
        students = kwargs.pop('students', Student.objects.none())
        super().__init__(*args, **kwargs)
        self.fields['student'].queryset = students



class AccessOTPForm(forms.Form):
    otp_code = forms.CharField(max_length=6, label='OTP Code')

class GenerateOTPForm(forms.Form):
    student_name = forms.CharField(label='Student Name', max_length=100)
    exam = forms.CharField(label='Exam Name', max_length=100)


class RegistrationForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    email = forms.EmailField(label='Email')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    role_choices = [
        ('Student', 'Student'),
        ('Lecturer', 'Lecturer'),
        ('Exam Admin', 'Exam'),
        ('Finance', 'Finance'),
        ('System Admin', 'System'),
    ]
    role = forms.ChoiceField(label='Role', choices=role_choices)

from django import forms
from .models import Student
from django import forms
from .models import Student
from django.contrib.auth.models import User

class StudentRecordForm(forms.ModelForm):
    user = forms.ModelChoiceField(queryset=User.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Student
        fields = ['user', 'student_id', 'name', 'email', 'phone', 'date_of_birth', 'address', 'department', 'courses', 'has_paid_fees', 'has_passed_semester_exams', 'phone_number', 'profile_photo']
        widgets = {
            'student_id': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'department': forms.Select(attrs={'class': 'form-control'}),
            'courses': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'has_paid_fees': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'has_passed_semester_exams': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'profile_photo': forms.FileInput(attrs={'class': 'form-control-file'}),
        }


class FeeRecordForm(forms.ModelForm):
    class Meta:
        model = FeeRecord
        fields = ['student', 'amount', 'date_paid']  # Add fields as needed
        widgets = {
            'student': forms.Select(attrs={'class': 'form-control'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'date_paid': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
'''        
class ExamCardForm(forms.ModelForm):
    class Meta:
        model = ExamCard
        fields = ['student', 'exam', 'issued', 'otp_code']
        widgets = {
            'student': forms.Select(attrs={'class': 'form-control'}),
            'exam': forms.Select(attrs={'class': 'form-control'}),
            'issued': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'otp_code': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(ExamCardForm, self).__init__(*args, **kwargs)
        self.fields['student'].label_from_instance = lambda obj: obj.name
        self.fields['exam'].label_from_instance = lambda obj: obj.exam_name

'''
# forms.py
# forms.py
from django import forms
from .models import ExamCard

class ExamCardForm(forms.ModelForm):
    class Meta:
        model = ExamCard
        fields = ['student', 'exam', 'issued', 'otp_code', 'units', 'year_of_study', 'exam_photo']
        widgets = {
            'student': forms.Select(attrs={'class': 'form-control'}),
            'exam': forms.Select(attrs={'class': 'form-control'}),
            'issued': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'otp_code': forms.TextInput(attrs={'class': 'form-control'}),
            'units': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'year_of_study': forms.NumberInput(attrs={'class': 'form-control'}),
            'exam_photo': forms.FileInput(attrs={'class': 'form-control-file'})
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Mark the exam_photo field as required
        self.fields['exam_photo'].required = True


    '''def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add student profile photo URL as initial data
        if self.instance and self.instance.student:
            self.initial['student_profile_photo_url'] = self.instance.student.profile_photo_url
'''