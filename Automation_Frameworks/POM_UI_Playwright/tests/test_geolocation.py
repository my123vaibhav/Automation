import pytest

from pages.geolocation_page import GeolocationPage

@pytest.mark.skip(reason="not implemented")
def test_geolocation(browser):
    geo_page = GeolocationPage(browser)
    geo_page.load()
    lat, lon = geo_page.get_location()
    assert lat != "" and lon != ""
