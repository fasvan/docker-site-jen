import os
import pytest
import requests

def url_ok():
    r = requests.head("http://127.0.0.1:8989/")
    assert r.text == "It works!"