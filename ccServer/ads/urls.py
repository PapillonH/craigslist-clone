from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_ad, name='create_ad'),
    path('edit/<int:ad_id>/', views.edit_ad, name='edit_ad'),
    path('list/', views.list_ads, name='list_ads'),
    path('view/<int:ad_id>/', views.view_ad, name='view_ad'),
]


from django.urls import include, path

urlpatterns = [
    # ... other URL patterns ...
    path('ads/', include('ads.urls')),
    # ... other URL patterns ...
]

