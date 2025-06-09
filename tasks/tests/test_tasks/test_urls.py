import pytest
from tasks.tests.test_tasks.fixture import *
from tasks.models import Task, TaskStatus
from rest_framework import status
from django.urls import reverse


@pytest.mark.django_db
def test_list_tasks(api_client, task):
    url = reverse("tasks:task-list")
    response = api_client.get(url, format="json")
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 1


@pytest.mark.django_db
def test_retrieve_tasks(api_client, task):
    url = reverse("tasks:task-item", args=[task.id])
    response = api_client.get(url, format="json")
    content = response.data
    assert response.status_code == status.HTTP_200_OK
    assert content.get("id") == task.pk
    assert content.get("title") == task.title


@pytest.mark.django_db
def test_create_task__valid(api_client):
    data = TaskFactory.build()
    task = {
        "title": data.title,
        "description": data.description,
    }
    url = reverse("tasks:task-create")
    response = api_client.post(
        path=url,
        data=task,
    )

    assert response.status_code == status.HTTP_201_CREATED
    assert Task.objects.all().count() == 1
    assert response.data.get("title") == task.get("title")


@pytest.mark.django_db
def test_create_task__invalid(api_client):
    task = {
        "title": TaskFactory.build().title,
    }
    url = reverse("tasks:task-create")
    response = api_client.post(
        path=url,
        data=task,
    )

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert Task.objects.all().count() == 0
    assert response.data["description"][0].code == "required"


@pytest.mark.django_db
def test_mark_as_complete(api_client, task):
    task.status = TaskStatus.PENDING
    task.save()

    assert Task.objects.first().status == TaskStatus.PENDING

    url = reverse("tasks:task-complete", args=[task.id])
    response = api_client.patch(path=url)
    assert Task.objects.first().status == TaskStatus.DONE
    assert response.status_code == status.HTTP_200_OK
    assert response.data["title"] == task.title


@pytest.mark.django_db
def test_delete_task(api_client, task):

    assert Task.objects.all().count() == 1

    url = reverse("tasks:task-destroy", args=[task.pk])
    response = api_client.delete(path=url)
    assert response.status_code == status.HTTP_200_OK
    assert response.data["title"] == task.title
    assert Task.objects.all().count() == 0
