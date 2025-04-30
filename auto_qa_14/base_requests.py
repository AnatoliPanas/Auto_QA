import requests

# base_url = "http://5.101.50.27:8000"
# creds = {"username": "harrypotter", "password": "expelliarmus"}


class CompanyApi:
    def __init__(self, url: str, creds: dict[str, str]):
        self.url = url
        self.creds = creds
        self.client_token = self.get_token()

    def get_token(self):
        url = self.url + '/auth/login'
        resp = requests.post(url, json=self.creds)
        assert resp.status_code == 200, "Что-то пошло не так!"
        return resp.json().get("user_token")

    def create_company(self, name: str, description: str = ""):
        url = self.url + '/company/create/'
        body = {
            'name': name,
            'description': description
        }
        resp = requests.post(url, json=body)
        assert resp.status_code == 201, "Что-то пошло не так!"
        return resp.json()

    def get_company(self, company_id):
        url = f"{self.url}/company/{company_id}"
        resp = requests.get(url)
        assert resp.status_code in (200, 404), "Что-то пошло не так!"
        return resp.json()

    def update_company(self, company_id, name: str, description: str = ""):
        url = f"{self.url}/company/update/{company_id}?client_token={self.client_token}"
        body = {
            'name': name,
            'description': description
        }
        resp = requests.patch(url, json=body)
        assert resp.status_code == 200, "Что-то пошло не так!"
        return resp.json()

    def delete_company(self, company_id):
        url = f"{self.url}/company/{company_id}?client_token={self.client_token}"
        resp = requests.delete(url)
        assert resp.status_code == 200, "Что-то пошло не так!"
        return resp.json()

    def get_company_list(self):
        url = f"{self.url}/company/list/"
        resp = requests.get(url)
        assert resp.status_code == 200, "Что-то пошло не так!"
        return resp.json()