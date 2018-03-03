
# from django.contrib import admin
from django.urls import path
import demo.dbviews
import demo.accountviews
import demo.views

urlpatterns = [
    path('index/', demo.views.index, name='home'),
    path('course/', demo.views.course),
    path('course_info/', demo.views.course_info),
    path('course_list/', demo.views.course_list),
    path('dbcourses/', demo.dbviews.db_course_list),
    path('add_course/', demo.dbviews.db_add_course),
    path('add_course_form/', demo.dbviews.db_form_add_course),
    path('add_book/', demo.views.add_book),
    path('home/', demo.accountviews.home, name='home'),
    path('list_accounts/', demo.accountviews.list_accounts, name='list_accounts'),
    path('add_account/', demo.accountviews.add_account, name='add_account'),

]
