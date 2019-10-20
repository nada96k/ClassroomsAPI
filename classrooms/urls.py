
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from classes import views as classes_views
from api import views as api_views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('classrooms/', classes_views.classroom_list, name='classroom-list'),
    path('classrooms/api/', api_views.ClassroomList.as_view(), name='list'),

    path('classrooms/<int:classroom_id>/', classes_views.classroom_detail, name='classroom-detail'),
    path('classrooms/<int:classroom_id>/api/', api_views.ClassroomDetails.as_view(), name='detail'),

    path('classrooms/create/', classes_views.classroom_create, name='classroom-create'),
    path('classrooms/create/api/', api_views.ClassroomCreateView.as_view(), name='create'),

    path('classrooms/<int:classroom_id>/update/', classes_views.classroom_update, name='classroom-update'),
    path('classrooms/<int:classroom_id>/update/api/', api_views.UpdateClassroom.as_view(), name='update'),

    path('classrooms/<int:classroom_id>/delete/', classes_views.classroom_delete, name='classroom-delete'),
    path('classrooms/<int:classroom_id>/delete/api/', api_views.DeleteClassroom.as_view(), name='delete'),

    
    path('login/', TokenObtainPairView.as_view(), name="login"),



]

if settings.DEBUG:
	urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
