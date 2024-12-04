from django.urls import path
from . import views
app_name = 'tweetapp'


urlpatterns = [
    path('', views.listtweet, name='listtweet'), #atilsamacioglu.com/tweetapp
    path('addtweet/', views.addtweet, name='addtweet'), #atilsamacioglu.com/tweetapp/addtweet
    path('addtweetbyform', views.addtweetbyform, name='addtweetbyform'), #atilsamacioglu.com/tweetapp/addtweetbyform
    path('addtweetbymodelform', views.addtweetbymodelform, name='addtweetbymodelform'), #atilsamacioglu.com/tweetapp/addtweetbymomdelform
    path('signup/', views.SignUpView.as_view(), name="signup"),
    path('deletetweet/<int:id>', views.deletetweet, name="deletetweet")
]