from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page),
    path('profiles/<int:pk>', views.exact_profile_html),
    path('search', views.search_profile),
    path('add_like/<int:pk>', views.add_like),
    path('add_dislike/<int:pk>', views.add_dislike),
    path('write_comment/<int:pr_id>/<int:ct_id>', views.write_comment),
    path('post_comment/<int:pr_id>/<int:ct_id>/<int:us_id>', views.post_comment),
    path('write_article', views.write_article),
    path('post_article/<int:pk>', views.post_article)

]