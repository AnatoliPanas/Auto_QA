import requests


# def user_update():
#     base_url = "http://5.101.50.27:8000"
#     data_json = {
#         "company_id": 1,
#         "email": "net1@net.net",
#         "phone": "+49987654321",
#     }
#     client_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJoYXJyeXBvdHRlciIsInJvbGUiOiJhZG1pbiIsImV4cCI6MTc0NTQxNDc5NH0.K3IqEndJDS_9E4qqahsrXMdqOcFGBVZ05PVgUw7jdUU"
#     response = requests.patch(f"{base_url}/employee/change/9/?client_token={client_token}", json=data_json)
#     print(response.status_code)
#     print(response.text)


def all_user_info():
    user_id = 100
    base_url = "http://5.101.50.27:8000"

    while True:
        response = requests.get(f"{base_url}/employee/info/{user_id}")

        if response.status_code == 200:
            print(f"User {user_id}:", response.json())
            user_id += 1
        else:
            break

all_user_info()