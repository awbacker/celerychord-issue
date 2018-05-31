from django.conf.urls import url

from cbug.apps.api.views import StartView

urlpatterns = [
    url('start/', StartView.as_view(), name="start")
]
