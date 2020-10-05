from server import __version__
from server.src import server
import pytest

def test_version():
    assert __version__ == '0.1.0'

@pytest.fixture
def client():
    server.app.config['TESTING'] = True
    with server.app.test_client() as client:
        yield client


def graph(client, slope, y_intercept):
    response = client.get('/api')
    assert b"Hello, World!" in response.data
