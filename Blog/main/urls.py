from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page),
    path('profiles/<int:pk>', views.exact_profile_html),
    path('search', views.search_profile),
    path('add_like/<int:pk>', views.add_like),
    path('add_dislike/<int:pk>', views.add_dislike),
]