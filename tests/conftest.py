from copy import deepcopy

import pytest
from fastapi.testclient import TestClient

from src import app as app_module


@pytest.fixture
def client():
    baseline_activities = deepcopy(app_module.activities)

    def restore_activities():
        app_module.activities.clear()
        app_module.activities.update(deepcopy(baseline_activities))

    restore_activities()
    with TestClient(app_module.app) as test_client:
        yield test_client
    restore_activities()
