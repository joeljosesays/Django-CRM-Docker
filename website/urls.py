from django.urls import path, include
from . import views
urlpatterns = [
    path('',views.home , name='home'),
    #path('login/',views.login_user,name='login'),
    path('logout/',views.logout_user,name='logout'),
    path('register/',views.register_user,name='register'),
    path('record/<int:pk>',views.customer_records,name='record'),
    path('delete/<int:pk>',views.delete_customer_record,name='delete'),
    path('add_record/',views.add_customer_record,name='add_record'),
    path('update_record/<int:pk>',views.update_customer_record,name='update_record')
]
