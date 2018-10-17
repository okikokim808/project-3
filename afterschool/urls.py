from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('', views.index, name='index'),
    path('account/', views.account, name='account'),
    path('about/', views.about, name='about'),
    path('account/', views.account, name='account'),
    path('account/daycare/', views.daycare_info, name='daycare'),
    path('staff/signout', views.student_signout, name='signout'),
    path('login', views.user_login, name="user_login"),
    path('logout', views.user_logout, name='logout'),
    path('staff/student_signin/',views.student_signin, name='student_signin'),
    path('staff/', views.staff, name='staff'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)