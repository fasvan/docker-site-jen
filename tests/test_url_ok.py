import os
import pytest
import requests

def test_get_homepage():
    r = requests.head("http://127.0.0.1:8989/")
    assert r.status_code == 204

def test_get_proxy_3000():
    r = requests.head("http://127.0.0.1:3000/")
    assert r.status_code == 204

def test_get_proxy_3001():
    r = requests.head("http://127.0.0.1:3001/")
    assert r.status_code == 204

def test_get_proxy_3002():
    r = requests.head("http://127.0.0.1:3002/")
    assert r.status_code == 204

def test_get_proxy_3003():
    r = requests.head("http://127.0.0.1:3003/")
    assert r.status_code == 204

def test_get_proxy_3004():
    r = requests.head("http://127.0.0.1:3004/")
    assert r.status_code == 204

def test_get_pgs_5432():
    r = requests.head("http://127.0.0.1:5432/")
    assert r.status_code == 204