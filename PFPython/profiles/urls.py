from django.urls import path
from .views import profile_view, delete_profile_view, update_profile_view, change_password_view
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', profile_view, name='profile'),
    path('delete/', delete_profile_view, name='delete_profile'),
    path('update-profile/', update_profile_view, name='update_profile'),
    path('change_password/', change_password_view, name='change_password'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
