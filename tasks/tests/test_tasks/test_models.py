import pytest
from tasks.tests.test_tasks.fixture import *
from tasks.models import Task, TaskStatus


@pytest.mark.django_db
def test_pending_status_by_default(task):
    task.status = None
    task.save()

    assert Task.objects.count() == 1
    assert Task.objects.first().status == TaskStatus.PENDING


@pytest.mark.django_db
def test_title_as_str(task):
    assert Task.objects.first().__str__() == task.title
