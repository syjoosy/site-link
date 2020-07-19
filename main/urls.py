from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage, name="home"),
    path('about/', views.aboutPage, name="about"),
    path('create-link/', views.createLinkPage, name="links"),
    # path('link/<slug>/', views.RedirectPage.as_view(), name='redirect-link')
    path('link/<slug>/', views.redirectPage, name="redirect-link")
]