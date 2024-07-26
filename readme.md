Create and deploy a running instance of a web server: Here's an Ansible playbook in Python that sets up a simple web server and serves the "Hello World" HTML page:
web_server.py file
To run this playbook, you'll need an Ansible control node and a managed node (the server where the web server will be deployed). Save the above code as a file as web_server.py and run the following command:
ansible-playbook -i <inventory-file> web_server.py
Replace <inventory-file> with the path to your Ansible inventory file, which contains the connection details for your managed node.

secure_web_server.py
In this playbook, we Configure the Apache web server to use a self-signed SSL certificate (you'll need to provide the paths to your self-signed certificate and key files using the ssl_cert_path and ssl_key_path arguments).
Enable the SSL module in Apache.
Enable the default-ssl site.
Add a redirect from HTTP to HTTPS.

Develop and apply automated tests to validate
To validate the server configuration, we can use a tool like Testinfra, which allows you to write infrastructure tests in Python.
validate.py
To run these tests, you'll need to have Testinfra installed on your Ansible control node. You can then run the tests using the following command
testinfra -v --connection=ansible --inventory-file=<inventory-file> validate.py






Run the playbook using the following command:

bash
ansible-playbook -i hosts deploy_webserver.yml


This command will connect to your server, install Apache, and deploy the index.html file with the specified content.

### Verification

After the playbook runs successfully, you can verify that your web server is up and running by navigating to http://your_server_ip in a web browser. You should see the following content:

html
<!DOCTYPE html>
<html>
<head>
  <title>My Web Server</title>
</head>
<body>
  <h1>Welcome to my web server!</h1>
  <p>This is a simple web page served by Apache.</p>
</body>
</html>
