
# from django.contrib import admin
from django.urls import path
import demo.views

urlpatterns = [
    path('index/', demo.views.index),
    path('course/', demo.views.course),

]
