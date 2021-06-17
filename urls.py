"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
#from quizapp import views
from django.urls import include, path
from . import views

#----Note: Every path adding before join - welcome,Ex: welcome/Subject/HomePage/admin - because this path include myproject url path-------#####




urlpatterns = [
    ##-------this path use for admin page----------

    path('Subject/HomePage/admin', admin.site.urls),
   
    ##--------this path use for Add Questions---------##

    path('Subject/HomePage/Add_Qus', views.Add_Questions),
    
    path('Delete/<id>', views.Delete_Qus),

    ##---------This path use for SchoolHomePage--------##

    path('Subject/HomePage/',views.schoolPage),

    ##---------This path use for SubjectPage-----------##

    path('HomePage/Subject/',views.Subject_Page),
    path('Subject/HomePage/SubjectPage/', views.Subject_Page),

    ##--------This path use for QuestionPage--------###
    path('Subject/<id>', views.Subject_Question_2),
    
]
#######-----http://127.0.0.1:8000/welcome/Subject/HomePage/---------#######