"""Role testing files using testinfra."""


def test_simple(host):
    command = """echo 'toto'"""
    cmd = host.run(command)
    assert 'toto' in cmd.stdout
