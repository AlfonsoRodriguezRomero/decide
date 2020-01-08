from django.urls import path
from . import views
from .views import voting_list,add_voting, edit_voting,delete_voting, add_question, question_list, delete_question


urlpatterns = [
   # path('', views.VotingView.as_view(), name='voting'),
    path('<int:voting_id>/', views.VotingUpdate.as_view(), name='voting'),
    path('', voting_list,name='list_voting'),
    path('add_voting/',add_voting,name="add_voting"),
    path('edit_voting/<int:id>',edit_voting),
    path('delete_voting/<int:id>',delete_voting),
    path('add_question/',add_question,name="add_question"),
    path('question/',question_list,name="list_question"),
    path('delete_question/<int:id>',delete_question),

]
