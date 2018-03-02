
# from django.contrib import admin
from django.urls import path
import demo.dbviews
import demo.views

urlpatterns = [
    path('index/', demo.views.index),
    path('course/', demo.views.course),
    path('course_info/', demo.views.course_info),
    path('course_list/', demo.views.course_list),
    path('dbcourses/', demo.dbviews.db_course_list),
    path('add_course/', demo.dbviews.db_add_course),
    path('add_course_form/', demo.dbviews.db_form_add_course),
    path('add_book/', demo.views.add_book),
    path('add_account/', demo.dbviews.add_account),

]
