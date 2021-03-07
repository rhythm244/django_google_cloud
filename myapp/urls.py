from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


app_name = 'myapp'

urlpatterns = [
    path('', views.index, name='index'),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path('person', views.person, name='person'),
    path('pilot_c130', views.pilot_c130, name='pilot_c130'),
    path('person/<int:employee_id>', views.person_one, name='person_one'),
    path('person_division/<int:division_id>', views.person_division, name='person_division'),
    path('upload/<int:employee_id>', views.upload, name='upload'),
    path('upload_employee/<int:employee_id>', views.upload_employee, name='upload_employee'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)