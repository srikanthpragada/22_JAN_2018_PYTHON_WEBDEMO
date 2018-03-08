
# from django.contrib import admin
from django.urls import path
import demo.dbviews
import demo.accountviews
import demo.views
import demo.cookie_views as cviews
import demo.session_views as sviews
import demo.rest_views as rest_views

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
    path('add_transaction/', demo.accountviews.add_transaction, name='add_transaction'),
    path('transactions/<int:id>', demo.accountviews.transactions_by_account,
             name='transactions'),
    path('edit_trans/<int:id>', demo.accountviews.edit_trans,
             name='edit_trans'),
    path('ajax/', demo.views.ajax),
    path('get_account_name/', demo.views.get_account_name),
    path('add_cookie/', cviews.add_cookie),
    path('list_cookies/', cviews.list_cookies),
    path('session_names/', sviews.list_names),
    path('accounts/', rest_views.list_accounts),
    path('accounts/<int:pk>', rest_views.get_account),

]
