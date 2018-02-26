from .dbmodel import DbCourse
from django.shortcuts import render

import sqlite3


def course_tuple_to_dbcourse(t):
    return DbCourse(t[0], t[1], t[2], t[3])


def db_course_list(request):
    con = None
    courses = []
    try:
        con = sqlite3.connect("db.sqlite3")
        cur = con.cursor()
        cur.execute("select * from courses order by id")
        for c in cur.fetchall():
            # convert tuple to Course object
            courses.append(course_tuple_to_dbcourse(c))
        cur.close()
    except Exception as ex:
        print(ex)
    finally:
        if con:
            con.close()

    return render(request, 'demo/db_course_list.html', {'courses': courses})


def db_add_course(request):
    message = ''
    if request.method == "POST":
        # process data
        title = request.POST["title"]
        duration = request.POST["duration"]
        fee = request.POST["fee"]
        print(title,duration,fee)
        # insert a row into COURSES
        con = None
        try:
            con = sqlite3.connect("db.sqlite3")
            cur = con.cursor()
            cur.execute("insert into courses (title,duration,fee) values(?,?,?)",
                         (title,duration,fee))
            if cur.rowcount == 1:
                con.commit()
                message = "Added Course Successfully!"

            cur.close()
        except Exception as ex:
            print(ex)
            message  = "Sorry! Could not add course!"
        finally:
            if con:
                con.close()

    else:
        print("Get Request")

    return render(request, 'demo/db_add_course.html', {"message" : message})