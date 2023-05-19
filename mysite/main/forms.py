from django import forms

from .models import Question_types



class Myform(forms.Form):
    question = forms.CharField(max_length=255,label='Question', widget=forms.TextInput(attrs={'class': 'form-input question'}))
    cat = forms.ModelChoiceField(queryset=Question_types.objects.values_list('q_type',flat=True), label="Category", empty_label="None")
    correct_answer = forms.CharField(label='Correct Answer',max_length=200, widget=forms.TextInput(attrs={'class': 'form-input answer','value':True}))
    incorrect_answer1 = forms.CharField(label='Incorrect Answer1',max_length=200, widget=forms.TextInput(attrs={'class': 'form-input answer'}))
    incorrect_answer2 = forms.CharField(max_length=200,label='Incorrect Answer2', widget=forms.TextInput(attrs={'class': 'form-input answer'}))
    incorrect_answer3 = forms.CharField(max_length=200,label='Incorrect Answer3', widget=forms.TextInput(attrs={'class': 'form-input answer'}))
    







  