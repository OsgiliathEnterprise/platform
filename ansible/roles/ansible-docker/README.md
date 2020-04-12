Containerization OverlayFS
=========

This role enriches the original [crivetimihai virtualization collection docker role](https://github.com/crivetimihai/ansible_virtualization/tree/master/roles/docker) and use the [Ansible manage lvm plus](https://github.com/OsgiliathEnterprise/ansible-manage-lvm-plus) role in order to add overlayfs driver support configuration on docker

Requirements
------------

Be sure on  Fedora 31 to set cgroup as v1 instead of the default v2 one:
```shell script
sudo dnf install -y grubby && \
  sudo grubby \
  --update-kernel=ALL \
  --args=”systemd.unified_cgroup_hierarchy=0"
```
See [this post for an explanation](https://fedoraproject.org/wiki/Changes/CGroupsV2)

You should first execute `./configure` first, which will download the requirements in siblings folders.
As this role is also using some roles coming from collections, you'll hale to update your ansible.cfg file:
roles_path = ./roles:./roles/community:./roles/community/ansible_collections/crivetimihai/roles


Molecule tests
--------------

To execute test, build your own Fedora-31 Packer image enabling cgroup V1 and call it platform/fedora-31.
Procedure:

```shell script
git clone git@github.com:chef/bento.git
cd "$(dirname ${BASH_SOURCE[0]})/bento/packer_templates/fedora-31"
sed -i -e "s/dnf -y install \(.*\)/dnf -y install \1 grubby \&\& grubby --update-kernel=ALL --args=\"systemd.unified_cgroup_hierarchy=0\" --make-default/" bento/packer_templates/fedora/scripts/install-supporting-packages.sh
packer build -var "box_basename=fedora-31-x86-64" -only=$PACKER_VM_DRIVER fedora-31-x86-64.json

cd "$(dirname ${BASH_SOURCE[0]})/bento/builds
vagrant box add fedora-31-x86_64.virtualbox.box --name platform/fedora-31
```

Role Variables
--------------

Only [dependencies variables](https://github.com/OsgiliathEnterprise/ansible-docker/blob/master/molecule/default/molecule.yml) at all but those of the dependencies, see [molecule tests](https://github.com/OsgiliathEnterprise/ansible-docker/blob/master/molecule/default/tests/test_default.py) for more info.

Dependencies
------------

As said
 * [crivetimihai virtualization collection](https://galaxy.ansible.com/crivetimihai/virtualization)
 * [Ansible manage lvm plus](https://galaxy.ansible.com/tcharl/ansible_manage_lvm_plus)

Example Playbook
----------------

See the [vars declared](https://github.com/OsgiliathEnterprise/ansible-docker/blob/master/molecule/default/molecule.yml) on the molecule test, as well as [their impact](https://github.com/OsgiliathEnterprise/ansible-docker/blob/master/molecule/default/tests/test_default.py) 


License
-------

[Apache-2](https://www.apache.org/licenses/LICENSE-2.0)

Author Information
------------------

* Twitter [@tcharl](https://twitter.com/Tcharl)
* Github [@tcharl](https://github.com/Tcharl)
* LinkedIn [Charlie Mordant](https://www.linkedin.com/in/charlie-mordant-51796a97/)
