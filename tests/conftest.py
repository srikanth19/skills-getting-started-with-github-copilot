"""Shared pytest fixtures for FastAPI backend tests."""

import copy

import pytest
from fastapi.testclient import TestClient

from src.app import activities, app

BASELINE_ACTIVITIES = copy.deepcopy(activities)


@pytest.fixture(autouse=True)
def reset_activities_state():
    """Reset in-memory activities data before each test for isolation."""
    activities.clear()
    activities.update(copy.deepcopy(BASELINE_ACTIVITIES))
    yield


@pytest.fixture
def client():
    """Create a FastAPI test client."""
    return TestClient(app)
