from django.conf.urls import patterns, include, url
from django.contrib import admin

from pybursa import views
from feedbacks.views import FeedbackView

urlpatterns = patterns('',
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.course_decr, name="index"),
    url(r'^contact/', views.contact, name="contact"),
    url(r'^student_list/', views.student_list, name="student_list"),
    url(r'^student_detail/', views.student_detail, name="student_detail"),
    url(r'^quadratic/results/', include('quadratic.urls', namespace="quadratic")),
    url(r'^courses/', include('courses.urls', namespace="courses")),
    url(r'^students/', include('students.urls', namespace="students")),
    url(r'^coaches/', include('coaches.urls', namespace="coaches")),
    url(r'^feedback/$', FeedbackView.as_view(), name='feedback'),
)
