from django.conf.urls import url
from django.urls import path, include

from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [

	# path('login/', views.user_login, name='login'),
	# 登入/登出
	path('login/', auth_views.login, name='login'),
    path('logout/', auth_views.logout, name='logout'),
    path('logout-then-login/', auth_views.logout_then_login, name='logout_then_login'),
    # 修改密碼
    path('password-change/', auth_views.password_change, name='password_change'),
    path('password-change/done/', auth_views.password_change_done, name='password_change_done'),
    # 重置密碼
    path('password-reset', auth_views.password_reset, name='password_reset'),
    path('password-reset/done/', auth_views.password_reset_done, name='password_reset_done'),
    path('password-reset/confirm/<slug:uidb64>/<slug:token>/', auth_views.password_reset_confirm, name='password_reset_confirm'),
    path('password-reset/complete/', auth_views.password_reset_complete, name='password_reset_complete'),
   	# 登入成功的dashboard
    path('', views.dashboard, name='dashboard'),
    # 註冊
    path('register/', views.register, name='register'),
    # 使用者編輯自己的資料
    path('edit/', views.edit, name='edit'),
    # 使用者列表
    path('users/', views.user_list, name='user_list'),
    # 使用者追蹤，須放在「使用者詳細資料」之前
    path('users/follow/', views.user_follow, name='user_follow'),
    # 使用者詳細資料
    path('users/<slug:username>/', views.user_detail, name='user_detail'),


    path('autoprofile/', views.autoprofile, name='autoprofile'),
    path('privacypolicy/', views.privacypolicy, name='privacypolicy'),

]