import requests

BASE_URL = 'http://127.0.0.1:3001'

def test_register():
    # Test registration endpoint
    register_data = {
        "first_name": "Test",
        "last_name": "User",
        "email": "tester@example.com",
        "password": "testpassword123"
    }
    
    response = requests.post(f'{BASE_URL}/auth/register', json=register_data)
    print("\nRegistration Response:", response.status_code)
    print(response.json())

def test_login():
    # Test login endpoint
    login_data = {
        "email": "tester@example.com",
        "password": "testpassword123"
    }
    
    response = requests.post(f'{BASE_URL}/auth/login', json=login_data)
    print("\nLogin Response:", response.status_code)
    print(response.json())

def test_update_profile():
    # First login to get the token
    login_data = {
        "email": "tester@example.com",
        "password": "testpassword123"
    }
    login_response = requests.post(f'{BASE_URL}/auth/login', json=login_data)
    token = login_response.json().get('token')
    
    # Test update profile endpoint
    update_data = {
        "first_name": "Updated",
        "last_name": "Name",
        "email": "tester@example.com",
        "old_password": "testpassword123"
    }
    headers = {'Authorization': f'Bearer {token}'}
    
    response = requests.put(f'{BASE_URL}/auth/update-profile', json=update_data, headers=headers)
    print("\nUpdate Profile Response:", response.status_code)
    print(response.json())

if __name__ == "__main__":
    test_register()
    test_login()
    test_update_profile()
