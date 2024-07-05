from django.urls import path
from . import views

app_name = 'tweetapp'

urlpatterns = [
    path("", views.listtweet, name='listtweet' ),  #esay.com/tweetapp/
    path("addtweet/", views.addtweet, name='addtweet' ), #esay.com/tweetapp/addtweet/
    path("addtweetbyform/", views.addtweetbyform, name='addtweetbyform' ), #esay.com/tweetapp/addtweetbyform/ 
    path('signup/', views.SignUpView.as_view(), name="signup"),
    path("deletetweet/<int:id>", views.deletetweet, name='deletetweet')
]



