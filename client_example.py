class FraudDetectionClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def test_endpoint(self, endpoint):
        import requests
        response = requests.get(f"{self.base_url}/{endpoint}")
        return response.json()  # Assuming the endpoint returns JSON

# Example usage:
if __name__ == '__main__':
    client = FraudDetectionClient('https://api.example.com')
    print(client.test_endpoint('test'))