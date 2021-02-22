from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


app_name = 'myapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('person', views.person, name='person'),
    path('person/<int:employee_id>', views.person_one, name='person_one'),
    path('person_division/<int:division_id>', views.person_division, name='person_division'),
    path('upload/<int:employee_id>', views.upload, name='upload'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)