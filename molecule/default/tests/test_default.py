import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_python3(host):
    cmd = host.run('python3 --version')
    assert cmd.rc == 0
    assert "Python 3" in cmd.stdout


def test_pip3(host):
    cmd = host.run('pip3 --version')
    assert cmd.rc == 0
    assert "python" in cmd.stdout
