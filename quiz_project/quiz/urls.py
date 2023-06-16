from django.urls import path

from quiz.views import quiz_list

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('list/',quiz_list),
]