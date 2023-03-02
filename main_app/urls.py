from django.urls import path
from . import views

urlpatterns = [
    # using an empty string here makes this our root route
    # views.home refers to a view that renders a file
    # the name='home' kwarg gives the route a name
    # naming routes is optional, but best practices
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    # paths for finches
    path('finches/', views.finches_index, name='index'),
    path('finches/<int:finch_id>/', views.finches_detail, name='detail'),
]