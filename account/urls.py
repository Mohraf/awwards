from django.urls import path, re_path
from . import views


app_name = 'account'

urlpatterns = [
  path('login/', views.LoginView.as_view(), name="login"),
  path('signup/', views.SignUpView.as_view(), name='signup'),
  path('logout/', views.logout_view, name='logout'),
  path(
      'users/',
      views.ListAccountView.as_view(),
      name='user_list'
  ),
  re_path(
      r'^(?P<username>[-\w]{5,30})/$',
      views.DetailAccountView.as_view(),
      name='profile'
  ),
  re_path(
      r'^(?P<username>[-\w]{5,30})/update/$',
      views.UpdateAccountView.as_view(),
      name='update'
  ),
  re_path(
      r'^(?P<username>[-\w]{5,30})/update/password/$',
      views.ChangePasswordView.as_view(),
      name='change_password'
  ),
]