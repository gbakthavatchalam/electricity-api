from django.test.utils import setup_test_environment
from django.test import Client
import pytest


@pytest.fixture(scope="session")
def client():
	setup_test_environment()
	yield Client()
