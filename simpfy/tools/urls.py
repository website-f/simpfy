from django.urls import path
from . import views

urlpatterns = [
    path('tools-index', views.tools_index, name='tools-index'),
    path('wolf', views.wolf, name="wolf"),
    path('wolfmath', views.wolfmath, name="wolfmath"),
    path('wolfweather', views.wolfweather, name="wolfweather"),
    path('wolfdel/<int:pk>', views.wolfdel, name="wolfdel"),
    path('wiki', views.wiki, name="wiki"),
    path('wikidel/<int:pk>', views.wikidel, name="wikidel"),
    path('wikihow', views.wikihow, name="wikihow"),
    path('wikihowres/<int:pk>', views.wikihowres, name="wikihowres"),
]