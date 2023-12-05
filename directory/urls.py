from django.urls import path
from directory.views import DirectionView, SiteListView, SiteLogRetrieveAPIView, SiteLogCreateView, SiteLogView

urlpatterns = [
    path('direction/', DirectionView.as_view()),
    path('site/all/', SiteListView.as_view()),
    path('site/log/<int:pk>/', SiteLogRetrieveAPIView.as_view()),
    path('site/log/add/', SiteLogCreateView.as_view()),
    path('site/log/all/', SiteLogView.as_view())
]
