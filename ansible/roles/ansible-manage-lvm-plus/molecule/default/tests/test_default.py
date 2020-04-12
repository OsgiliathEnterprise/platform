"""Role testing files using testinfra."""


def test_lvm_package_shall_be_installed(host):
    assert host.package("lvm2").is_installed


def test_non_persistent_volume_group_is_created(host):
    command = """sudo vgdisplay | grep -c 'non-persistent'"""
    cmd = host.run(command)
    assert '1' in cmd.stdout


def test_thinpool_logical_volume_is_created(host):
    command = """sudo lvs -o lv_name  non-persistent --separator='|' --noheadings | grep -c 'thinpool'"""
    cmd = host.run(command)
    assert int(cmd.stdout.rstrip()) >= 1


def test_thinpoolmeta_logical_volume_is_created(host):
    command = """sudo lvs -o metadata_lv  non-persistent --separator='|' --noheadings | grep -c 'thinpool_tmeta'"""
    cmd = host.run(command)
    assert '1' in cmd.stdout


def test_thinpool_profile_autoextends_treshold_is_set(host):
    command = """cat /etc/lvm/profile/non-persistent-thinpool.profile | grep -c 'thin_pool_autoextend_threshold=80'"""
    cmd = host.run(command)
    assert '1' in cmd.stdout


def test_thinpool_profile_autoextends_percent_is_set(host):
    command = """cat /etc/lvm/profile/non-persistent-thinpool.profile | grep -c 'thin_pool_autoextend_percent=20'"""
    cmd = host.run(command)
    assert '1' in cmd.stdout


def test_thinpool_is_monitored(host):
    command = """sudo lvs -o+seg_monitor | grep -c 'monitored'"""
    cmd = host.run(command)
    assert '1' in cmd.stdout
# Don't know how to test autoextend


def test_formating_is_xfs(host):
    command = """sudo xfs_info /dev/non-persistent/thinpool | grep -c 'ftype=1'"""
    cmd = host.run(command)
    assert '1' in cmd.stdout


def test_xfs_volume_is_mounted(host):
    host.file("/var/lib/docker").mode == 0o731

