import pytest

def pytest_collection_modifyitems(config, items):
    for item in items:
        if "performance_tests" in item.nodeid:
            item.add_marker(pytest.mark.benchmark)