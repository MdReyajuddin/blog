from django.urls import path
from subsribe import views
urlpatterns = [
    path('', views.mail_send_view),
]