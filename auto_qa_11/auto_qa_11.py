import requests

base_url = "http://5.101.50.27:8000"


def test_simple_req():
    resp = requests.get('http://5.101.50.27:8000/company/list')
    assert resp.status_code == 200  # Проверяем, что сервер вернул статус 200 (OK)


def test_auth():
    user_data = {
        "username": "harrypotter",
        "password": "expelliarmus"
    }
    responce = requests.post(f"{base_url}/auth/login", json=user_data)
    assert responce.json()['user_token'] is not None
    assert responce.status_code == 200

def test_create_company():
 company = {
 "name": "python",
 "description": "requests"
 }
 resp = requests.post(base_url + '/company/create', json=company)
 assert resp.status_code == 201 # 201 означает, что компания успешно создана

