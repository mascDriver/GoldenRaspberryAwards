import pytest
from fastapi import status


def test_get_producer_intervals(client, sample_movies):
    """Test the GET /awards/intervals endpoint"""
    response = client.get("/awards/intervals")
    
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    
    assert "min" in data
    assert "max" in data
    assert isinstance(data["min"], list)
    assert isinstance(data["max"], list)
    
    min_intervals = data["min"]
    if len(min_intervals) > 0:
        found_john = False
        for interval in min_intervals:
            if interval["producer"] == "John Producer" and interval["interval"] == 1:
                found_john = True
                assert interval["previousWin"] == 1980
                assert interval["followingWin"] == 1981
        assert found_john, "John Producer with interval 1 should be in min intervals"
    
    max_intervals = data["max"]
    if len(max_intervals) > 0:
        found_jane = False
        for interval in max_intervals:
            if interval["producer"] == "Jane Producer" and interval["interval"] == 5:
                found_jane = True
                assert interval["previousWin"] == 1985
                assert interval["followingWin"] == 1990
        assert found_jane, "Jane Producer with interval 5 should be in max intervals"


def test_get_producer_intervals_empty_db(client):
    """Test the GET /awards/intervals endpoint with an empty database"""
    response = client.get("/awards/intervals")
    
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    
    assert "min" in data
    assert "max" in data
    assert isinstance(data["min"], list)
    assert isinstance(data["max"], list)
    assert len(data["min"]) == 0
    assert len(data["max"]) == 0
