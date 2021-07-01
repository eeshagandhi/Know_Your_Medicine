from django import forms
from .models import medicine_data,post,Category,comment

choices=Category.objects.all().values_list('name','name')
list=[]
for i in choices:
    list.append(i)
class MedForm(forms.ModelForm):
    class Meta:
        model=medicine_data
        fields=['SNo', 'Disease', 'Prescribed_medicine', 'Dosage', 'Side_Effects', 'Patient_Review', 'Price']
        widgets={
            'SNo':forms.TextInput(attrs={'class':'form-control','readonly':'readonly'}),
            'Disease':forms.TextInput(attrs={'class':'form-control','readonly':'readonly'}),
            'Prescribed_medicine':forms.TextInput(attrs={'class':'form-control','readonly':'readonly'}),
            'Dosage':forms.TextInput(attrs={'class':'form-control'}),
            'Side_Effects':forms.TextInput(attrs={'class':'form-control'}),
            'Patient_Review':forms.TextInput(attrs={'class':'form-control'}),
            'Price':forms.TextInput(attrs={'class':'form-control'}),
            #'Feedback':forms.Textarea(attrs={'class':'form-control'}),
        }
class CommentForm(forms.ModelForm):
    class Meta:
        model=comment
        fields=['name','body']
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'body':forms.Textarea(attrs={'class':'form-control'}),
        }
class FeedbackForm(forms.ModelForm):
    class Meta:
        model=medicine_data
        fields=['Disease', 'Prescribed_medicine','Dosage','Side_Effects','Price']
        widgets={
            'Disease':forms.TextInput(attrs={'class':'form-control'}),
            'Prescribed_medicine':forms.TextInput(attrs={'class':'form-control'}),
            'Dosage':forms.TextInput(attrs={'class':'form-control'}),
            'Side_Effects':forms.TextInput(attrs={'class':'form-control'}),
            'Price':forms.TextInput(attrs={'class':'form-control'}),
            #'Feedback':forms.Textarea(attrs={'class':'form-control'}),
        }
class MedSearchForm(forms.ModelForm):
    class Meta:
        model=medicine_data
        fields=['Prescribed_medicine','Disease']
class AddForm(forms.ModelForm):
    class Meta:
        model=post
        fields=('title','author','category','body')
        widgets={
            'title': forms.TextInput(attrs={'class':'form-control'}),
            #'author': forms.Select(attrs={'class':'form-control'}),
            'author': forms.TextInput(attrs={'class':'form-control', 'value':'', 'id':'eesha', 'type':'hidden'}),
            'category':forms.Select(choices=list,attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class':'form-control'}),
        }
class EditForm(forms.ModelForm):
    class Meta:
        model=post
        fields=('title','author','category','body')
        widgets={
            'title': forms.TextInput(attrs={'class':'form-control'}),
            #'author': forms.Select(attrs={'class':'form-control'}),
            'author': forms.TextInput(attrs={'class':'form-control', 'value':'', 'id':'eesha', 'type':'hidden'}),
            'category':forms.Select(choices=list,attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class':'form-control'}),
        }

       