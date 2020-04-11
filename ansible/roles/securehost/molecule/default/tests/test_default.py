"""Role testing files using testinfra."""

def test_fail2ban_is_installed(host):
    command = """dnf list installed fail2ban | grep -c 'fail2ban'"""
    cmd = host.run(command)
    assert '1' in cmd.stdout


def test_fail2ban_is_running(host):
    command = """systemctl status fail2ban | grep -c 'active (running)'"""
    cmd = host.run(command)
    assert '1' in cmd.stdout
