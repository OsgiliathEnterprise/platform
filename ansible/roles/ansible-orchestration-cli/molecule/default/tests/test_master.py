"""Role testing files using testinfra."""
testinfra_hosts = ["master.osgiliath.test"]


def test_namespace_is_created(host):
    command = r"""
    kubectl get ns | \
    grep -c istio-system"""
    with host.sudo():
        cmd = host.run(command)
        assert '1' in cmd.stdout
