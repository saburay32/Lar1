from django.contrib import admin
from django.urls import path,include
from users import views as userViews
from django.contrib.auth import views as authViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('reg/',userViews.register,name='reg'),
    path('user/',authViews.LoginView.as_view,name='auth'),
    path('', include('blog.urls')),
]
