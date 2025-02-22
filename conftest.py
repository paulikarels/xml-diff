import pytest

def pytest_configure(config):
    if not config.getoption("--benchmark-only"):
        setattr(config.option, "markexpr", "not benchmark")
