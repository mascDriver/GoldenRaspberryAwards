from fastapi import status


def test_read_root(client):
    """Test the root endpoint of the application"""
    response = client.get("/")
    
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"message": "Olá Mundo!"}


def test_health_check(client):
    """Test that the API is up and running"""
    response = client.get("/")
    assert response.status_code == status.HTTP_200_OK
