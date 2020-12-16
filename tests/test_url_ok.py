import os
import pytest
import requests

def test_get_homepage():
    r = requests.head("http://127.0.0.1:8989/")
    assert r.status_code == 200

def test_get_homepage_204():
    r = requests.head("http://127.0.0.1:8989/")
    assert r.status_code == 204

def test_get_homepage_3000_200():
    r = requests.head("http://127.0.0.1:3000/")
    assert r.status_code == 200

def test_get_homepage_3001_204():
    r = requests.head("http://127.0.0.1:3001/")
    assert r.status_code == 204