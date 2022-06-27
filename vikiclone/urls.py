from django.urls import path
from . import views

urlpatterns = [
    path('',views.all,name="home"),
    path('search/',views.search,name="search"),
    path('add/',views.add,name="add"),
    path('entry/<str:id>/',views.one,name="one"),
    path('entry/<str:id>/edit',views.edit,name="edit"),
    path('entry/<str:id>/remove',views.remove,name="remove"),
    path('login/',views.login_user,name="login"),
    path('logout/',views.logout_user,name="logout")
]