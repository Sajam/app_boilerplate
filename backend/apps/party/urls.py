from django.conf.urls import url
import views

urlpatterns = [
    url(r'^all/$', views.PartyView.as_view(), name='party'),
]

