from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import view_api, views

# from .view_api import BlacklistTokenUpdateView

app_name = 'myapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('preflight', views.preflight, name="preflight"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path('pilot_c130/', views.pilot_c130, name='pilot_c130'),
    path('person/<int:employee_id>', views.person_one, name='person_one'),
    path('person_division/<int:division_id>', views.person_division, name='person_division'),
    path('upload/<int:employee_id>', views.upload, name='upload'),
    path('upload_employee/<int:employee_id>', views.upload_employee, name='upload_employee'),

    path('lessonlearn', views.lessonlearn, name='lessonlearn'),
    path('lessonlearn_form', views.lessonlearn_form, name='lessonlearn_form'),
    path('lessonlearn_info/<int:id>',views.lessonlearn_info, name='lessonlearn_info'),
    # path('upload_lessonlearn', views.upload_lessonlearn, name='upload_lessonlearn'),

    #API javascript
    path('pilot_c130/<int:page>', views.pilot_c130_page, name='pilot_c130_page'),
    path('lessonlearn_filter/<int:airport_id>', views.lessonlearn_filter, name='lessonlearn_filter'),
    path('lessonlearn_filter_one/<int:pk>', views.lessonlearn_filter_one, name='lessonlearn_filter_one'),
    path('airport/', views.airport, name='airport'),
    path('weather_key', views.weather_key, name='weather_key'),

    #API for react
    # path('login_react', view_api.login_react, name='login_react'),
    # path('logout_react', view_api.logout_react, name='logout_react'),
    # path('api/employees/', view_api.api_employees, name="api_employees"),
    # path('logout/blacklist/', BlacklistTokenUpdateView.as_view(),
    #      name='blacklist')
] 


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# print(f'This is : {settings.MEDIA_URL}')

    