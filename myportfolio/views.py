from django.shortcuts import render,get_object_or_404,redirect
from django.http import FileResponse, HttpResponse,HttpRequest
from projects.models import Projects
from blogs.models import Blog,Comment
from django.core.signing import Signer
from experience.models import Responsibility,Experience
import os
from django.conf import settings

def home(request):
    return render(request=request,template_name='index.html')


def projects(request):
    projects=Projects.objects.all()
    return render(request,'projects.html',{'projects':projects})

def project(request,project_id):
    project=get_object_or_404(Projects,pk=project_id)
    return render(request,'project.html',{'project':project})

def blogs(request):
    blogs=Blog.objects.all()
    return render(request,'blogs.html',{'blogs':blogs})


def addLike(request,blog_id):
    if request.method == 'POST':
        blog = get_object_or_404(Blog, pk=blog_id)
        # Retrieve liked_posts cookie or create an empty string
        liked_posts = request.COOKIES.get('liked_posts','')
        signer = Signer()
        signed_post_id = signer.sign(str(blog_id))
        print(signed_post_id)
        print(liked_posts.split(";"))
        if signed_post_id not in liked_posts.split(";"):
            # Add the post_id to the cookie
            blog = Blog.objects.get(pk=blog_id)
            blog.like_count += 1
            blog.save()
            liked_posts += f"{signed_post_id};"
            response = HttpResponse('Cookie is set!')
            response.set_cookie('liked_posts', liked_posts, max_age=31536000)  # Set cookie expiration
            return redirect('blogs')
    return HttpResponse("Failed to like post!")

def addComment(request,blog_id):
    if request.method == 'POST':
        blog = Blog.objects.get(pk=blog_id)
        comment_text = request.POST['blog_comment']
        Comment.objects.create(blog_id=blog, blog_comment=comment_text)
    return redirect('blogs')

def show_all_comments(request,id):
    blog=Blog.objects.get(pk=id)
    return render(request,'allcomments.html',{'blog':blog})
def experience(request):
    experiences=Experience.objects.all()
    return render(request,'experience.html',{'experiences':experiences})
