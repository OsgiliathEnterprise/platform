"""Role testing files using testinfra."""


def test_389_ds_is_installed(host):
    command = """rpm -qa | grep 389-ds"""
    cmd = host.run(command)
    assert '389-ds' in cmd.stdout
