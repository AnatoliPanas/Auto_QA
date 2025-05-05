import requests


class TestEmployeeApi:
    base_url = "http://5.101.50.27:8000"
    client_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJoYXJyeXBvdHRlciIsInJvbGUiOiJhZG1pbiIsImV4cCI6MTc0NjQ1ODkxM30.Elw9ExSKMizCP4TJM-DWqzJeSQ7jymkBZuhG_DI7OQs"

    def test_user_create(self):
        data_json = {
            "first_name": "Анатолий",
            "last_name": "Панас",
            "middle_name": "Александрович",
            "company_id": 615,
            "email": "net@net.net",
            "phone": "+49123456789",
            "birthdate": "1986-01-25",
            "is_active": True
        }

        response = requests.post(f"{self.base_url}/employee/create/", json=data_json)
        assert response.status_code == 200

    def test_user_info(self):
        user_id = 9

        response = requests.get(f"{self.base_url}/employee/info/{user_id}")
        assert response.status_code == 200

    def test_user_update(self):
        data_json = {
            "company_id": 1,
            "email": "net1@net.net",
            "phone": "+49987654321",
        }

        response = requests.patch(f"{self.base_url}/employee/change/1/?client_token={self.client_token}", json=data_json)
        assert response.status_code == 200