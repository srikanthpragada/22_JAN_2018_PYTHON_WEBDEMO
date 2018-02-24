
# from django.contrib import admin
from django.urls import path
import demo.views

urlpatterns = [
    path('index/', demo.views.index),
    path('course/', demo.views.course),
    path('course_info/', demo.views.course_info),
    path('course_list/', demo.views.course_list),

]
