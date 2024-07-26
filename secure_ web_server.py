from ansible.module_utils.basic import AnsibleModule

def main():
    module = AnsibleModule(
        argument_spec={
            'html_content': {
                'type': 'str',
                'default': '<html><head><title>Hello World</title></head><body><h1>Hello World!</h1></body></html>'
            },
            'ssl_cert_path': {
                'type': 'str',
                'required': True
            },
            'ssl_key_path': {
                'type': 'str',
                'required': True
            }
        }
    )

    html_content = module.params['html_content']
    ssl_cert_path = module.params['ssl_cert_path']
    ssl_key_path = module.params['ssl_key_path']

    tasks = [
        {
            'name': 'Install Apache',
            'apt': {
                'name': 'apache2',
                'state': 'present'
            }
        },
        {
            'name': 'Copy HTML file',
            'copy': {
                'content': html_content,
                'dest': '/var/www/html/index.html'
            }
        },
        {
            'name': 'Configure Apache for HTTPS',
            'lineinfile': [
                {
                    'path': '/etc/apache2/sites-available/default-ssl.conf',
                    'regexp': '^#?\s*SSLCertificateFile',
                    'line': f'SSLCertificateFile {ssl_cert_path}'
                },
                {
                    'path': '/etc/apache2/sites-available/default-ssl.conf',
                    'regexp': '^#?\s*SSLCertificateKeyFile',
                    'line': f'SSLCertificateKeyFile {ssl_key_path}'
                }
            ]
        },
        {
            'name': 'Enable SSL module',
            'apache2_module': {
                'name': 'ssl',
                'state': 'present'
            }
        },
        {
            'name': 'Enable default-ssl site',
            'apache2_vhost': {
                'name': 'default-ssl',
                'state': 'present',
                'enabled': 'true'
            }
        },
        {
            'name': 'Redirect HTTP to HTTPS',
            'lineinfile': {
                'path': '/etc/apache2/sites-available/000-default.conf',
                'regexp': '^#?\s*Redirect\s+permanent\s+/\s+',
                'line': 'Redirect permanent / https://$server_name'
            }
        },
        {
            'name': 'Start Apache',
            'systemd': {
                'name': 'apache2',
                'state': 'started',
                'enabled': 'yes'
            }
        }
    ]

    module.run_commands(tasks)
    module.exit_json(changed=True)

if __name__ == '__main__':
    main()
