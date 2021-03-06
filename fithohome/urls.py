from .import views
from django.urls import path


urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("homepage", views.homepage, name="homepage"),
    path("signup", views.signup, name="signup"),
    path("login", views.login, name="login"),
    path("aboutus", views.aboutus, name="aboutus"),
    path("blog", views.blog, name="blog"),
    path("userform", views.inputform, name="userform"),
    path("renting", views.renting, name="renting"),
    path("logout", views.logout, name="logout"),
    path("rentingform", views.rentingformdata, name="renting"),
    path("approvment", views.app, name="app"),
    path("training", views.train, name="training"),
]
