from django.shortcuts import render, redirect
from . import models
from django.urls import reverse, reverse_lazy
from tweetapp.forms import AddTweetForm
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView

def listtweet(request):
    all_tweets = models.Tweet.objects.all()
    tweet_dict = {"tweets":all_tweets}
    return render(request, 'tweetapp/listtweet.html', context=tweet_dict)


def addtweet(request):
    # print(request.POST)
    """
    if request.POST:
        print(request.POST["username"])
        print(request.POST["message"])
    """
    if request.POST:
        message = request.POST["message"]
        models.Tweet.objects.create(username = request.user, message = message)
        return redirect(reverse('tweetapp:listtweet'))
    else:
        return render(request, 'tweetapp/addtweet.html')


def addtweetbyform(request):
    if request.method == "POST":
        form = AddTweetForm(request.POST)
        if form.is_valid():
            nickname = form.cleaned_data['nickname_input']
            message = form.cleaned_data['message_input']
            models.Tweet.objects.create(nickname=nickname, message=message)
        
            return redirect(reverse('tweetapp:listtweet'))
        else:
            print("error in form!")
            return render(request, "tweetapp/addtweetbyform.html", context={'form':form})
    else:
        form = AddTweetForm()
        return render(request, "tweetapp/addtweetbyform.html", context={'form':form})
    

def deletetweet(request, id):
    tweet = models.Tweet.objects.get(pk=id)
    if request.user == tweet.username:
        models.Tweet.objects.filter(id=id).delete()
        return redirect("tweetapp:listtweet")
    

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"






