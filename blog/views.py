from django.shortcuts import render
from .models import Post

#Sample Post Data
#posts = [
#        {
#            'author' :'Clinton Dmello',
#            'title':'Blog Post 1',
#            'content':'First post content',
#            'date_posted':'January 25,2020'
#      },
#      {
#            'author' :'Swebert Dmello',
#            'title':'Blog Post 2',
#            'content':'Second post content',
#            'date_posted':'January 26,2020'
#      }
#      ]

def home(request):
    context = {
        'posts':Post.objects.all()
        }
    return render(request,'blog/home.html',context) #Should return HttpResponse or an Expection

def about(request):
    return render(request,'blog/about.html',{'title':'About'})