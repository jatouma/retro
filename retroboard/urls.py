from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register_view, name="register"),
    path("submit", views.submit_view, name="submit"),
    path("actions", views.actions_view, name="actions"),
    path("complete", views.complete_view, name="complete"),
    path("export", views.export_view, name="export")
]