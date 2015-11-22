from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^comparasion/', views.comparasion, name="comparasion"),
    url(r'^$', views.portfolio, name="portfolio"),
    url(r'^secondary_chart/', views.get_sub_chart, name="secondary_chart"),
]
