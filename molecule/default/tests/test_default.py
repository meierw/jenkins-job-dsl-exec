import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_jenkins(host):
    output = host.check_output(get_script_curl_command('hello.groovy'))
    assert output == 'hello world'

    output = host.check_output(get_script_curl_command('version.groovy'))
    assert output == '2.4.12'


def get_script_curl_command(script_file):
    script_dir = os.path.dirname(__file__) + '/scripts/'
    script_content = open(script_dir + script_file, 'r').read()

    # script passed in 'single quotes', so scripts themselves should avoid using them
    return (
        'curl -u admin:admin ' +
        "--data-urlencode 'script=" + script_content + "' " +
        'http://localhost:8080/scriptText'
    )
