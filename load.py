import requests
import time

# Define the endpoint of your application
url = 'http://localhost:8080'  # Adjust this URL

# Function to make HTTP requests
def send_request():
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print('Request sent successfully!')
        else:
            print(f"Received unexpected status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error making request: {e}")

# Run load test continuously
def load_test(interval=0.01, duration=600):
    start_time = time.time()
    
    while time.time() - start_time < duration:
        send_request()
        time.sleep(interval)  # Adjust this value to control request frequency

    print('Load test completed!')

# Run the load test for 600 seconds with requests every 0.1 seconds
load_test(interval=0.01, duration=600)