import testinfra

def test_apache_is_installed(host):
    assert host.package("apache2").is_installed

def test_html_page_is_served(host):
    response = host.run("curl http://localhost")
    assert "Hello World!" in response.stdout

def test_http_redirects_to_https(host):
    response = host.run("curl http://localhost")
    assert response.rc == 301
    assert "https://" in response.stdout

def test_https_serves_content(host):
    response = host.run("curl https://localhost")
    assert "Hello World!" in response.stdout
