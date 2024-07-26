from ansible.module_utils.basic import AnsibleModule

def main():
    module = AnsibleModule(
        argument_spec={
            'html_content': {
                'type': 'str',
                'default': '<html><head><title>Hello World</title></head><body><h1>Hello World!</h1></body></html>'
            }
        }
    )

    html_content = module.params['html_content']

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
