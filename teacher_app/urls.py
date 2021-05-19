from django.urls import path, include

from rest_framework.routers import DefaultRouter
from teacher_app import views


router= DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')
router.register('profile', views.UserProfileViewSet)
router.register('studnet', views.StudentViewSet)
router.register('teacher', views.TeacherViewSet)
router.register('staff', views.StaffViewSet)

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
    path('login/', views.UserLoginApiView.as_view()),
    path('',include(router.urls))
]
