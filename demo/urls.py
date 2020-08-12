from django.urls import path
from demo import views

urlpatterns = [
    path('', views.login),
    path('login', views.login),
    path('registartion',views.registration),
    path('addData',views.addData),
    path('viewdata',views.viewData),
    path('editdata',views.editData),
    path('deletedata',views.deleteData),
    path('loginD',views.loginD),
    path('logout', views.logout),
    path('loginDashboard',views.Dashboard)
    
]