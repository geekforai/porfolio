"""
URL configuration for myportfolio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path
from myportfolio import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home,name='home'),
    path('projects/', views.projects,name='projects'),
     path('blogs/', views.blogs,name='blogs'),
    path('projects/<int:project_id>/', views.project, name='project_detail'),
    path('like/<int:blog_id>/', views.addLike, name='like_blog'),
    path('comment/<int:blog_id>/', views.addComment, name='add_comment'),
    path('blog/<int:id>/', views.show_all_comments, name='show_all_comments'),
    path('experiences/', views.experience, name='experiences'),
 
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
