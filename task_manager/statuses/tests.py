from django.test import TestCase
from django.urls import reverse_lazy
from task_manager.users.models import User
from .models import Status


USER = {
    'username': 'eren-yeager',
    'password': 'attacktitan',
}

STATUS_ONE = {'name': 'The Fall of Shiganshina'}
STATUS_TWO = {'name': 'The Basement'}
STATUS_THREE = {'name': 'The Town Where Everything Began'}


class StatusesTest(TestCase):

    url_login = reverse_lazy('login')
    url_status_create = reverse_lazy('create_status')
    url_status_update = reverse_lazy('update_status', args=[1])
    url_status_delete = reverse_lazy('delete_status', args=[1])

    def setUp(self):
        self.user = User.objects.create_user(**USER)
        self.client.post(self.url_login, data=USER)
        self.client.post(self.url_status_create, data=STATUS_ONE)

    def test_status_read(self):
        status = Status.objects.get(id=1)
        self.assertEqual(status.name, 'The Fall of Shiganshina')

    def test_status_create(self):
        self.client.post(self.url_status_create, data=STATUS_TWO)
        status = Status.objects.get(id=2)
        self.assertEqual(status.name, 'The Basement')

    def test_status_update(self):
        self.client.post(self.url_status_update, data=STATUS_THREE)
        status = Status.objects.get(id=1)
        self.assertEqual(status.name, 'The Town Where Everything Began')

    def test_status_delete(self):
        self.client.post(self.url_status_delete)
        self.assertEqual(Status.objects.count(), 0)
