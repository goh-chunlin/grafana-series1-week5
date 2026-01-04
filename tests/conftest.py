import pytest
import responses

@pytest.fixture
def validate_o11y_headers():
    with responses.RequestsMock() as rsps:
        yield rsps
