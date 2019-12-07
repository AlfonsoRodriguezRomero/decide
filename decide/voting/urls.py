from django.urls import path
from . import views 
from .views import voting_list,add_voting, edit_voting


urlpatterns = [
   # path('', views.VotingView.as_view(), name='voting'),
    path('<int:voting_id>/', views.VotingUpdate.as_view(), name='voting'),
    path('', voting_list,name='list_voting'),
    path('add_voting/',add_voting,name="add_voting"),
    path('edit_voting/<int:id>',edit_voting)
]
 