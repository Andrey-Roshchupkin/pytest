import requests
from faker import Faker

fake = Faker()
BASE_URL = "http://localhost:5000/api/user/"

class TestUserEndpoint:

    def test_get_user_by_id(self):
        name = fake.name()
        email = fake.email()
        response = requests.post("http://localhost:5000/api/users/", json={"name": name, "email": email})
        user_id = response.json()["id"]
        response = requests.get(BASE_URL + str(user_id))
        assert response.status_code == 200
        response_json = response.json()
        assert response_json["id"] == user_id
        assert response_json["name"] == name
        assert response_json["email"] == email

    def test_get_non_existent_user(self):
        response = requests.get(BASE_URL + "999999999")
        assert response.status_code == 404
        assert "User not found" in response.json()["message"]

    def test_update_user(self):
        name = fake.name()
        email = fake.email()
        response = requests.post("http://localhost:5000/api/users/", json={"name": name, "email": email})
        user_id = response.json()["id"]
        new_name = fake.name()
        new_email = fake.email()
        response = requests.patch(BASE_URL + str(user_id), json={"name": new_name, "email": new_email})
        assert response.status_code == 200
        response_json = response.json()
        assert response_json["id"] == user_id
        assert response_json["name"] == new_name
        assert response_json["email"] == new_email

    def test_update_non_existent_user(self):
        new_name = fake.name()
        new_email = fake.email()
        response = requests.patch(BASE_URL + "999999999", json={"name": new_name, "email": new_email})
        assert response.status_code == 404
        assert "User not found" in response.json()["message"]

    def test_delete_user(self):
        name = fake.name()
        email = fake.email()
        response = requests.post("http://localhost:5000/api/users/", json={"name": name, "email": email})
        user_id = response.json()["id"]
        response = requests.delete(BASE_URL + str(user_id))
        assert response.status_code == 200
        response = requests.get(BASE_URL + str(user_id))
        assert response.status_code == 404
        assert "User not found" in response.json()["message"]

    def test_delete_non_existent_user(self):
        response = requests.delete(BASE_URL + "99999")
        assert response.status_code == 404
        assert "User not found" in response.json()["message"]