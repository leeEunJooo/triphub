# accounts urls.py
from django.urls import path
from django.contrib.auth import views as auth_view
from .views import register
from .views import activate
# import Rooms.views as room


urlpatterns = [
    path('login/', auth_view.LoginView.as_view(), name="login"),
    path('logout/', auth_view.LogoutView.as_view(template_name ='login.html'), name="logout"),
    path('register/', register, name="register"),
    path('activate/<slug:uid64>/<slug:token>/', activate, name ="activate"), 
    # path('login_done', login_done, name = "login_done"),
]