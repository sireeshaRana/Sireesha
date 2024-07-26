import requests

def test_http_to_https_redirect():
    response = requests.get("http://<your-instance-public-ip>")
    assert response.history[0].status_code == 301
    assert response.url.startswith("https://")

def test_hello_world_page():
    response = requests.get("https://<your-instance-public-ip>")
    assert response.status_code == 200
    assert "<h1>Hello World!</h1>" in response.text
