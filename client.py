import requests

server_ip = "172.20.5.2"  # Replace with VM1's IP
url = "http://" + server_ip + ":8080/"

try:
    response = requests.get(url)
    print("Response from server:", response.text)
except requests.exceptions.RequestException as e:
    print("Error connecting to server:", e)

