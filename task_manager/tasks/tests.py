from django.test import TestCase
from django.urls import reverse_lazy
from task_manager.users.models import User
from .models import Task

USER = {
    'username': 'eren-yeager',
    'password': 'attacktitan',
}

STATUS_ONE = {
    'name': 'To You, 2,000 Years From Now'
}

STATUS_TWO = {
    'name': 'From You, 2,000 Years Ago'
}

STATUS_THREE = {
    'name': 'Guilty Shadow'
}

LABEL_ONE = {
    'name': 'A Dream I Once Had'
}

LABEL_TWO = {
    'name': 'Delusions of Strength'
}

LABEL_THREE = {
    'name': 'Euthanasia plan by Zeke Yeager'
}

TASK_ONE = {
    'name': 'The Battle of Heaven and Earth',
    'description': 'Mentally sent a message using the Founding Titan',
    'status': 1,
    'labels': 1,
}

TASK_TWO = {
    'name': 'Toward the Tree on That Hill',
    'description': 'Afterwards, Paradis is destroyed by war',
    'status': 2,
    'labels': 2,
}

TASK_THREE = {
    'name': 'Titans',
    'description': 'Life is pointless since to live also means to eventually die',
    'status': 3,
    'labels': 3,
}


class TasksTest(TestCase):

    url_login = reverse_lazy('login')
    url_status_create = reverse_lazy('create_status')
    url_label_create = reverse_lazy('create_label')
    url_task_create = reverse_lazy('create_task')
    url_task_update = reverse_lazy('update_task', args=[1])
    url_task_delete = reverse_lazy('delete_task', args=[1])

    def setUp(self):
        self.user = User.objects.create_user(**USER)
        self.client.post(self.url_login, data=USER)
        self.client.post(self.url_status_create, data=STATUS_ONE)
        self.client.post(self.url_status_create, data=STATUS_TWO)
        self.client.post(self.url_status_create, data=STATUS_THREE)
        self.client.post(self.url_label_create, data=LABEL_ONE)
        self.client.post(self.url_label_create, data=LABEL_TWO)
        self.client.post(self.url_label_create, data=LABEL_THREE)
        self.client.post(self.url_task_create, data=TASK_ONE)

    def test_task_read(self):
        task = Task.objects.get(id=1)
        self.assertEqual(task.name, 'The Battle of Heaven and Earth')
        self.assertEqual(task.status.name, 'To You, 2,000 Years From Now')
        self.assertEqual(task.description, 'Mentally sent a message using the Founding Titan')
        self.assertEqual(task.labels.all()[0].name, 'A Dream I Once Had')

    def test_task_create(self):
        self.client.post(self.url_task_create, data=TASK_TWO)
        task = Task.objects.get(id=2)
        self.assertEqual(task.name, 'Toward the Tree on That Hill')
        self.assertEqual(task.status.name, 'From You, 2,000 Years Ago')
        self.assertEqual(task.description, 'Afterwards, Paradis is destroyed by war')
        self.assertEqual(task.labels.all()[0].name, 'Delusions of Strength')

    def test_task_update(self):
        self.client.post(self.url_task_update, data=TASK_THREE)
        task = Task.objects.get(id=1)
        self.assertEqual(task.name, 'Titans')
        self.assertEqual(task.status.name, 'Guilty Shadow')
        self.assertEqual(task.description, 'Life is pointless since to live also means to eventually die')
        self.assertEqual(task.labels.all()[0].name, 'Euthanasia plan by Zeke Yeager')

    def test_task_delete(self):
        self.client.post(self.url_task_delete)
        self.assertEqual(Task.objects.count(), 0)
