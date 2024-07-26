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
