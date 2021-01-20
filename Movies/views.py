from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from .models import Movie
from . import forms
import pandas as pd
from . import utils
from .MLmodel import LinearRegressionTraining
import joblib
import requests
import json

reloadModel = joblib.load('Movies\MLmodel\DecisionTreeClassifier.pk1')

def index(request):
    movies = Movie.objects.all()
    return render(request, 'Index.html', {'movies': movies})

def score(request):
    if request.method=='POST':
        temp = {}
        temp['Sex'] = request.POST.get('Sex')
        temp['SibSp'] = request.POST.get('SibSp')
        temp['Parch'] = request.POST.get('Parch')
        temp['Pclass'] = request.POST.get('Pclass')
        temp['Age']=request.POST.get('Age')
        temp['Fare']=request.POST.get('Fare')
        temp['Embarked']=request.POST.get('Embarked')
    testdata = pd.DataFrame({'x':temp}).transpose()

    newdata = utils.encode_input(testdata)
    predictedRating = reloadModel.predict(newdata)[0]
    if predictedRating == 1:
        predictedRating = True
    else:
        predictedRating = False

    context = {'rating': predictedRating}
    
    return  render(request, 'Prediction.html', context)

def SurvivalLaujk(request):
    form = forms.SurvivalForm()
    return render(request, 'Prediction.html', {'form': form})
