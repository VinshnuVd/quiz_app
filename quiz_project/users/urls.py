from django.urls import path

from users.views import register_view

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('register/',register_view),
]