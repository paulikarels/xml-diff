def pytest_configure(config):
    """Configures pytest to exclude 'benchmark' marked tests if '--benchmark-only' is specified."""
    if not config.getoption("--benchmark-only"):
        setattr(config.option, "markexpr", "not benchmark")
