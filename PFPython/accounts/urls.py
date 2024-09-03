from django.urls import path
from accounts.views import signup_view, login_view, logout_view,home_view, update_profile_view
urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('home/',home_view, name='home'),
    path('update-profile/', update_profile_view, name='update_profile'),
    path('update-profile/', update_profile_view, name='update_profile'),
]
