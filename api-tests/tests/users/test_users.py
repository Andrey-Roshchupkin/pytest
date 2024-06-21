import requests
from faker import Faker

fake = Faker()
BASE_URL = "http://localhost:5000/api/users/"

class TestUsersEndpoint:
    def test_get_users(self):
        response = requests.get(BASE_URL)
        assert response.status_code == 200
        data = response.json()
        for user in data:
            assert 'id' in user
            assert 'name' in user
            assert 'email' in user

    def test_post_user(self):
        name = fake.name()
        email = fake.email()
        response = requests.post(BASE_URL, json={"name": name, "email": email})
        assert response.status_code == 201
        response_json = response.json()
        assert response_json["name"] == name
        assert response_json["email"] == email

    def test_create_user_missing_email_field(self):
        name = fake.name()
        response = requests.post(BASE_URL, json={"name": name})
        assert response.status_code == 400
        message = response.json()["message"]
        assert "Email cannot be blank" in message['email']       

    def test_create_user_duplicate_email(self):
        name1 = fake.name()
        email = fake.email()
        name2 = fake.name()
        requests.post(BASE_URL, json={"name": name1, "email": email})
        response = requests.post(BASE_URL, json={"name": name2, "email": email})
        assert response.status_code == 500