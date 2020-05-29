from main import get_temperature
import requests
import pytest


class MockResponse:  # Create Mock with static method return temperature value

    @staticmethod
    def json():
        return {'currently': {'temperature': 62}}


@pytest.mark.parametrize("lat, lng, expect", [(14.235004, -51.92528, 16)])  # parametrize values lat, lng and expect
def test_get_temperature_by_lat_lng(monkeypatch, lat, lng, expect):

    def mock_get(*args, **kwargs):  # create function mock_get return Mock Response, this code based in example Pytest Documentation section Monkeypatch
        return MockResponse()

    monkeypatch.setattr(requests, "get", mock_get)

    result = get_temperature(lat, lng)
    assert result == expect
