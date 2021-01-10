import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_is_docker_installed(host):
    package_docker = host.package('docker-ce')
    assert package_docker.is_installed


def test_container_registry_is_running(host):
    command = """docker ps | \
            egrep -c 'registry:2.*healthy'"""
    with host.sudo():
        cmd = host.run(command)
        assert int(cmd.stdout.rstrip()) >= 1


def test_nginx_is_up(host):
    command = """curl http://containers.dummy.com/ | \
            grep -c 'html'"""
    cmd = host.run(command)
    assert int(cmd.stdout.rstrip()) >= 1
