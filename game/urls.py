from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('guess/<int:game_id>/', views.guess_letter, name='guess'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
