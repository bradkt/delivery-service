"""The tests to run in this project.
To run the tests type,
$ nosetests --verbose --nocapture
or  for windows
python -m nose --verbose --nocapture
"""

from nose.tools import assert_true
import requests

# BASE_URL = "http://127.0.0.1"
BASE_URL = "http://localhost:5000"


def test_get_list_request():
    "Test getting a list"
    response = requests.get(
        '%s/list/%s' % (BASE_URL, '8ANYAfOG38OvBulBfxoHQcrpY1k2'))
    assert_true(response.ok)


def test_get_list_request_404():
    "Test getting a non existent list"
    response = requests.get('%s/list/%s' % (BASE_URL, 'an_incorrect_id'))
    assert_true(response.status_code == 404)


def test_add_new_list():
    "Test adding a new list"
    payload = {"randString1": {"value": "apples", "note": "red", "quantity": 5},
               "randString2": {"value": "banana", "note": "ripe", "quantity": 6}}
    response = requests.post(
        '%s/list/%s' % (BASE_URL, '8ANYAfOG38OvBulBfxoHQcrpY1k2'), json=payload, headers={"Content-Type": "application/json"})
    assert_true(response.status_code == 201)


def test_update_list():
    "Test update a list"
    payload = {"randString1": {"value": "apples", "note": "red", "quantity": 5},
               "randString2": {"value": "banana", "note": "ripe", "quantity": 11}}
    response = requests.put('%s/list/%s' %
                            (BASE_URL, '8ANYAfOG38OvBulBfxoHQcrpY1k2'), json=payload)
    assert_true(response.status_code == 200)


def test_update_list_no_user_id():
    "Test updating a list with no user id"
    payload = {"randString1": {"value": "apples", "note": "red", "quantity": 5},
               "randString2": {"value": "banana", "note": "ripe", "quantity": 6}}
    response = requests.put('%s/list/%s' % (BASE_URL, ''), json=payload)
    assert_true(response.status_code == 404)


def test_clear_list():
    "Test clearing list"
    response = requests.delete('%s/list/%s' %
                               (BASE_URL, '8ANYAfOG38OvBulBfxoHQcrpY1k2'))
    assert_true(response.status_code == 200)


def test_clear_list_404():
    "Test clearing list fail"
    response = requests.delete('%s/list/%s' %
                               (BASE_URL, ''))
    assert_true(response.status_code == 404)
