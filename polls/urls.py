from django.urls import path

from . import views
from django.views.generic import TemplateView

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    # ex: /polls/about
#    path('about/', TemplateView.as_view(template_name="polls/about.html")), 
    path('about/', views.AboutView.as_view()),
    # ex: /polls/5/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # ex: /polls/5/results/
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
