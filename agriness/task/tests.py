from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import Task
from datetime import datetime


class TaskViewSetTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.task1 = Task.objects.create(name='Task 1', description='Task 1 description')
        self.task2 = Task.objects.create(name='Task 2', description='Task 2 description')
        self.task3 = Task.objects.create(name='Task 3', description='Task 3 description', finished_at=datetime.now())

    def test_get_task(self):
        response = self.client.get('/task/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 3)

    def test_filter_tasks_by_done_status(self):
        url = reverse('task-list')

        # Filtrar tarefas concluídas
        response = self.client.get(url, {'is_done': 'True'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['id'], self.task3.id)

        # Filtrar tarefas não concluídas
        response = self.client.get(url, {'is_done': 'False'})
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['id'], self.task1.id)

    def test_create_task(self):
        url = reverse('task-list')
        data = {'name': 'Task 4', 'description': 'Task 4 description'}

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 4)
        self.assertEqual(Task.objects.last().name, 'Task 4')

    def test_update_task(self):
        url = reverse('task-detail', kwargs={'pk': self.task1.id})
        data = {'name': 'New Task', "description": "New description"}

        response = self.client.put(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.task1.refresh_from_db()
        self.assertEqual(self.task1.name, 'New Task')
        self.assertEqual(self.task1.description, 'New description')

    def test_delete_task(self):
        url = reverse('task-detail', kwargs={'pk': self.task1.id})

        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Task.objects.count(), 2)
        self.assertFalse(Task.objects.filter(id=self.task1.id).exists())


