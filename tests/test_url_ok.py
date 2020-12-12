import os
import pytest
import requests

def url_ok("http://127.0.0.1:8989/"):
    r = requests.head("http://127.0.0.1:8989/")
    return r.status_code == 200
