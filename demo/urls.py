
from django.urls import path
from .views import *

app_name = 'demo'

urlpatterns = [
    path('test/', Test),
    path('', Login, name= "login"),
    path('logout/', view_logout, name= "logout"),
    path('dashboard/', Dashboard, name= "dashboard"),
    path('<int:question_id>/', detail, name='detail'),
    path('<int:question_id>/results/',results, name='results'),
    path('<int:question_id>/vote/', vote, name='vote'),
    path('question/save/', save_question_result, name='save-question-result'),
]