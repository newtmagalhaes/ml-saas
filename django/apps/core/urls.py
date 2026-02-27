from django.urls import path

from . import views

app_name = 'core'

urlpatterns = [
    path('', views.QuestionListView.as_view(), name="question_list_view"),
    path('<int:id>/', views.QuestionDetailView.as_view(), name="question_detail_view"),
]
