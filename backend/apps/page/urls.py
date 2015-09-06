from django.conf.urls import url
import views

urlpatterns = [
    url(r'^(?P<slug>[\w-]+)/$', views.PageView.as_view(), name='page'),
]

