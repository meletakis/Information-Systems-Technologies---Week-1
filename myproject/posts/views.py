from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
import json
import urllib2

@login_required
def index(request):
     data = json.load(urllib2.urlopen('http://jsonplaceholder.typicode.com/posts'))
     context = {'data' : data}
     return render(request, 'allposts.html', context)
@login_required
def getpost(request, postid):
     post = json.load(urllib2.urlopen('http://jsonplaceholder.typicode.com/posts/'+postid))
     comments = json.load(urllib2.urlopen('http://jsonplaceholder.typicode.com/posts/'+postid+'/comments' ))
     context = {'post' : post, 'comments':comments}
     return render(request, 'post.html', context)
@login_required
def getuser(request, userid):
     user = json.load(urllib2.urlopen('http://jsonplaceholder.typicode.com/users/'+userid))
     user_posts= json.load(urllib2.urlopen('http://jsonplaceholder.typicode.com/posts?userId='+userid))
     context = {'user' : user,'user_posts' : user_posts }
     return render(request, 'user.html', context)