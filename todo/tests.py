from django.test import TestCase
from django.contrib.auth.models import User
from .models import Task


class TaskModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create(username='testuser')

    def setUp(self):
        self.task = Task.objects.create(
            user=self.user,
            title='Test Task',
            description='This is a test task',
            complete=False
        )

    def test_str_representation(self):
        self.assertEqual(str(self.task), 'Test Task')

    def test_default_complete_value(self):
        self.assertFalse(self.task.complete)

    def test_ordering(self):
        task2 = Task.objects.create(
            user=self.user,
            title='Another Task',
            description='This is another task',
            complete=True
        )
        task3 = Task.objects.create(
            user=self.user,
            title='Third Task',
            description='This is the third task',
            complete=False
        )
        tasks = Task.objects.all()
        self.assertEqual(tasks[0], self.task)
        self.assertEqual(tasks[1], task3)
        self.assertEqual(tasks[2], task2)
