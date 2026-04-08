import requests

BASE_URL = 'http://127.0.0.1:5000'

def test_endpoint(name, method, path, json_data=None):
    url = f"{BASE_URL}{path}"
    print(f"Testing {name:15} | {method:4} | {url}")
    try:
        if method == 'GET':
            response = requests.get(url)
        elif method == 'POST':
            response = requests.post(url, json=json_data)
        elif method == 'PUT':
            response = requests.put(url, json=json_data)
        
        if response.status_code in [200, 201]:
            print(f"  ✅ Success: {response.json()}")
        else:
            print(f"  ❌ Failed: {response.status_code}")
    except requests.exceptions.ConnectionError:
        print("  ❌ Connection Error: Is the Flask server running? Run 'flask run' first.")

if __name__ == '__main__':
    print("--- Starting Dev Environment Health Check ---\n")
    # Mapping our 4 key modules
    # Use 'username' and 'password' to match the Flask app logic
    test_endpoint("Auth Login", "POST", "/auth/login", {"username": "admin", "password": "password123"})
    test_endpoint("Catalog List", "GET",  "/catalog/products")
    test_endpoint("Order History","GET",  "/orders/history/user123")
    test_endpoint("Profile Bio",  "PUT",  "/profile/update-bio", {"bio": "Hello AI!"})
