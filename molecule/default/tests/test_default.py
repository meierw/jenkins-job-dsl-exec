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
    return (
        'curl -u admin:admin ' +
        '--data-urlencode "script=$(cat ' + os.environ['JENKINS_TEST_SCRIPT_DIR'] + '/' + script_file + ')" ' +
        'http://localhost:8080/scriptText'
    )
