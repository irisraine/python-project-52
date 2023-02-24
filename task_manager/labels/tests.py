from django.test import TestCase
from django.urls import reverse_lazy
from task_manager.users.models import User
from .models import Label


USER = {
    'username': 'eren-yeager',
    'password': 'attacktitan',
}

LABEL_ONE = {'name': 'Sole Salvation'}
LABEL_TWO = {'name': 'Descent'}
LABEL_THREE = {'name': 'Perfect Game'}


class LabelsTest(TestCase):

    url_login = reverse_lazy('login')
    url_label_create = reverse_lazy('create_label')
    url_label_update = reverse_lazy('update_label', args=[1])
    url_label_delete = reverse_lazy('delete_label', args=[1])

    def setUp(self):
        self.user = User.objects.create_user(**USER)
        self.client.post(self.url_login, data=USER)
        self.client.post(self.url_label_create, data=LABEL_ONE)

    def test_label_read(self):
        label = Label.objects.get(id=1)
        self.assertEqual(label.name, 'Sole Salvation')

    def test_label_create(self):
        self.client.post(self.url_label_create, data=LABEL_TWO)
        label = Label.objects.get(id=2)
        self.assertEqual(label.name, 'Descent')

    def test_label_update(self):
        self.client.post(self.url_label_update, data=LABEL_THREE)
        label = Label.objects.get(id=1)
        self.assertEqual(label.name, 'Perfect Game')

    def test_label_delete(self):
        self.client.post(self.url_label_delete)
        self.assertEqual(Label.objects.count(), 0)
