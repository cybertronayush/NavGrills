from django.urls import path,include
from django.contrib import admin
from quiz import views
from django.contrib.auth.views import LogoutView,LoginView
urlpatterns = [
   
    path('admin/', admin.site.urls),
    path('teacher/',include('teacher.urls')),
    path('student/',include('student.urls')),
    


    path('',views.home_view,name=''),
    path('logout', LogoutView.as_view(template_name='quiz/logout.html'),name='logout'),
    path('aboutus', views.aboutus_view),
    path('contactus', views.contactus_view),
    path('afterlogin', views.afterlogin_view,name='afterlogin'),


    
    path('admin-dashboard', views.admin_dashboard_view,name='admin-dashboard'),
    


]
