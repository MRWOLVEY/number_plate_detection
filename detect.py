import requests

url = "http://127.0.0.1:8000/detect"
files = {"file": open("test.jpg", "rb")}  # Replace with your image path

response = requests.post(url, files=files)
print(response.json())  # Should return plate number & color