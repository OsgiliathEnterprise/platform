import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_is_docker_installed(host):
    package_docker = host.package('docker-ce')
    assert package_docker.is_installed


def test_run_hello_world_container_successfully(host):
    with host.sudo():
        hello_world_ran = host.run("docker run hello-world")
    assert 'Hello from Docker!' in hello_world_ran.stdout


def test_docker_storage_is_overlay2(host):
    command = """sudo docker info | grep -c 'overlay2'"""
    cmd = host.run(command)
    assert '1' in cmd.stdout


def test_docker_group_exists(host):
    command = """sudo cat /etc/group | grep -c 'docker'"""
    cmd = host.run(command)
    assert '1' in cmd.stdout
