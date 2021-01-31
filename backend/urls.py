"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from tutor import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('login/', views.login),
    path('signup/',views.signup),
    path('pro1/<int:pk>',views.proOne),
    path('pro2/<int:pk>',views.proTwo),
    path('search/',views.search),
    path('chat/',views.chat),
    path('myclasses/',views.myclasses),
    path('messages/',views.messages),
    path('notification/',views.notification),
    path('contactSupport/',views.contactSupport),
    path('alluser/',views.task),
    path('user/<int:pk>',views.user_api),
    path('sndRegister', views.sndRegister, name='sndRegister'),
    path('sendOtp', views.sendOtp),
    path('send_otp', views.send_otp),
    path('allclass/',views.class_task),
    path('class/<int:pk>',views.class_api),
    path('allconnect/',views.connect_task),
    path('connect/<int:pk>',views.connect_api),
    path('allcnctmsg/',views.connect_msgtask),
    path('connectmsg/<int:pk>',views.connect_msgapi),
    path('allconnectmsgatt/',views.connect_msg_attachtask),
    path('connectmsgatt/<int:pk>',views.connect_msg_Attachapi),

]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
