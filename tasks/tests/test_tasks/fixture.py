import pytest
import factory
from rest_framework.test import APIClient
from tasks.models import Task, TaskStatus


class TaskFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Task

    title = factory.Faker("sentence")
    description = factory.Faker("paragraph")
    status = TaskStatus.PENDING


@pytest.fixture
def api_client():
    client = APIClient()
    return client


@pytest.fixture
def task():
    return TaskFactory.create()


@pytest.fixture
def tasks(amount):
    return TaskFactory.create_batch(amount)
