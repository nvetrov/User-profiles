from common.views import index, RegisterView, CreateUserProfile
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.urls import path
from allauth.account.views import login, logout

app_name = 'common'
urlpatterns = [
    path('', index, name='index'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    # path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    # path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(
        template_name='register.html',
        success_url=reverse_lazy('common:profile-create')
    ), name='register'),
    path('profile-create/', CreateUserProfile.as_view(), name='profile-create'),
]

# from common.views import index #, login, logout
# from django.urls import path
# from django.contrib.auth.views import LoginView, LogoutView
#
# app_name = 'common'
# urlpatterns = [
#     path('', index, name='index'),
#     # path('login/', login, name='login'),
#     path('login/', LoginView.as_view(template_name='login.html'), name='login'),
#     # path('logout/', logout, name='logout'),
#     path('logout/', LogoutView.as_view(), name='logout'),
# ]
