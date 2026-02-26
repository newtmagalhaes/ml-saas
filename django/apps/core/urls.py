from django.urls import path

from . import views

app_name = 'core'

urlpatterns = [
    path('', views.PredictView.as_view(), name="predict_view"),
    path('form/', views.DiabetesFormView.as_view(), name="diabetes_form_view"),
]
