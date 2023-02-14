from django.urls import path

from task_manager.users.views import UserCreateView, UsersListView

urlpatterns = [
    path('', UsersListView.as_view(), name='users_list'),
    path('create/', UserCreateView.as_view(), name='create_user')
]