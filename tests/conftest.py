"""Shared pytest fixtures for the backend API tests."""

import copy

import pytest
from fastapi.testclient import TestClient

from src import app as app_module
from src.app import app


@pytest.fixture
def client():
    """Provide a FastAPI TestClient for the application."""
    return TestClient(app)


@pytest.fixture(autouse=True)
def reset_activities():
    """Isolate tests by snapshotting and restoring the in-memory activities."""
    snapshot = copy.deepcopy(app_module.activities)
    yield
    app_module.activities.clear()
    app_module.activities.update(snapshot)
