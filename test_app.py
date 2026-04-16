import pytest
from app import app
from dash.testing.application_runners import import_app

def test_header_present(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("h1", timeout=10)
    assert dash_duo.find_element("h1").text != ""

def test_visualisation_present(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#pinkmorsel-over-time", timeout=10)
    assert dash_duo.find_element("#pinkmorsel-over-time") is not None

def test_region_picker_present(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#radio-items", timeout=10)
    assert dash_duo.find_element("#radio-items") is not None