from django.urls import path
from login_app import views



app_name='login_app'

urlpatterns = [
    path('signup/', views.sign_up, name='signup'),
    path('login/', views.Sign_in, name='signin'),
    path('logout/', views.logout_page, name='logout'),
    path('profile/', views.profile_page, name='profile'),
    path('password/', views.pass_change, name='pass_change'),
    path('profile_pic_upload/', views.add_pro_pic, name='profile_pic_upload'),
    path('profile_pic_change/', views.change_pro_pic, name='profile_pic_change'),
    path('update_profile/', views.edit_profile_information, name='update_profile'),
]


