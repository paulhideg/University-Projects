from __future__ import print_function
from flask import json
import requests
from sqlalchemy.exc import NoSuchColumnError


"""
    {
        username: string
        password: string
        role: "user" | "admin"
    }
"""

BASE = "http://localhost:5000"
HEADERS = {'Content-type': 'application/json'}
# location given here
location = "delhi technological university"
  

def login(body):
    url = BASE + "/login/"
    data = json.dumps(body)
    r = requests.post(url = url, data = json.dumps(body), headers=HEADERS)
    data = r.json()
    return data["session_id"]

def test_user_login():
    body = {
                "username": "user",
                "password": "user",
                "role": "user"
            }
    assert login(body) is not None
    print("test_user_login PASSED")


def test_admin_login():
    body = {
                "username": "admin",
                "password": "admin",
                "role": "admin"
            }
    assert login(body) is not None
    print("test_admin_login PASSED")

def test_add_to_bucket_list():
    login_body = {
                "username": "user",
                "password": "user",
                "role": "user"
            }

    body = {
        "session_id": login(login_body),
        "title": "Title",
        "description": "description",
        "image": "image",
        "geolocation": "geolocation",
        "start_date": "starte_date",
        "end_date": "end_date"
        }

    url = BASE + "/user/add"
    data = json.dumps(body)
    r = requests.put(url = url, data = json.dumps(body), headers=HEADERS)
    data = r.json()
    assert data["id"] is not None
    print("test_add_to_bucket_lis PASSED")


if __name__ == "__main__":
    test_user_login()
    test_admin_login()
    test_add_to_bucket_list()

