from django.test import TestCase
from django.urls import reverse_lazy
from .models import User


USER = {
    'username': 'eren-yeager',
    'password': 'attacktitan',
}

USER_ONE = {
    'first_name': 'Mikasa',
    'last_name': 'Akkerman',
    'username': 'mikasa-akkerman',
    'password1': 'azumabito',
    'password2': 'azumabito',
}
USER_TWO = {
    'first_name': 'Armin',
    'last_name': 'Arlert',
    'username': 'armin-arlert',
    'password1': 'colossaltitan',
    'password2': 'colossaltitan',
}
USER_THREE = {
    'first_name': 'Levi',
    'last_name': 'Akkerman',
    'username': 'levi-akkerman',
    'password1': 'no-regrets',
    'password2': 'no-regrets',
}


class UsersTest(TestCase):

    url_register = reverse_lazy('create_user')
    url_login = reverse_lazy('login')
    url_user_update = reverse_lazy('update_user', args=[1])
    url_user_delete = reverse_lazy('delete_user', args=[1])

    def setUp(self):
        self.user = User.objects.create_user(**USER)

    def test_user_register(self):
        initial_users_count = User.objects.count()
        self.client.post(self.url_register, data=USER_ONE)
        self.client.post(self.url_register, data=USER_TWO)
        self.assertEqual(User.objects.count(), initial_users_count + 2)

    def test_user_login(self):
        self.client.post(self.url_login, data=USER)
        auth_id = self.client.session['_auth_user_id']
        self.assertEqual(User.objects.get(pk=auth_id).username, 'eren-yeager')

    def test_user_update(self):
        self.client.post(self.url_login, data=USER)
        self.client.post(self.url_user_update, data=USER_THREE)
        self.assertEqual(User.objects.get(pk=1).username, 'levi-akkerman')

    def test_user_delete(self):
        self.client.post(self.url_login, data=USER)
        self.client.post(self.url_user_delete)
        self.assertEqual(User.objects.count(), 0)
