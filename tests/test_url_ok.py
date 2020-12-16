import os
import pytest
import requests

def test_get_homepage():
    r = requests.head("http://127.0.0.1:8989/")
    assert r.status_code == 200