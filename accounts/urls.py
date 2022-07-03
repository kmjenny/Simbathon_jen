from django.urls import path, include
from .views import *
from . import views
from rest_framewrok import urls

app_name = "accounts"

urlpatterns = [
    path('home/signup/', signup, name='signup'),
    path('home/login/', login, name='login'),
    path('home/logout/', logout, name='logout'),
    path('home/', home, name='home'),
    path('activate/<str:uidb64>/<str:token>', Activate.as_view()),
    path('signup/', views.UserCreate.as_view()),
    path('api-auth/', include('rest_framework.urls')),
]