import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
    data = response.get_json()
    assert data['message'] == "Welcome to CI/CD Demo App!"
    assert data['status'] == "ok"

def test_health(client):
    response = client.get('/api/health')
    assert response.status_code == 200
    data = response.get_json()
    assert data['status'] == "healthy"
    assert data['version'] == "1.0.0"

def test_users(client):
    response = client.get('/api/users')
    assert response.status_code == 200
    data = response.get_json()
    assert len(data['users']) == 2
    assert data['users'][0]['name'] == "Alice"
    assert data['users'][1]['name'] == "Bob"