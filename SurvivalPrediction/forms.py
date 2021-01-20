from django import forms

class SurvivalForm(forms.Form):
    
    Sex = forms.CharField()
    Parch = forms.IntegerField()
    Fare = forms.IntegerField()
    Embarked = forms.CharField()
    Pclass = forms.IntegerField()
    Age = forms.IntegerField()
    SibSp = forms.IntegerField()