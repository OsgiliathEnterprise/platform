Lvm-manager
=========

This role is an extension of the [most used lvm cookbook](https://github.com/mrlesmithjr/ansible-manage-lvm).
It add the ability to create thinpools

Role Variables
--------------

In addition to the [usual variables](https://github.com/mrlesmithjr/ansible-manage-lvm/blob/master/README.md), you can declare some more.
```yaml
---
lvnames:
  ...
  metadata: <another lvname> # declares the metadata logical volume 
```

```yaml
---
lvnames:
  ...
  autoextendtreshold: <number> # threshold of the autoextend profile
  autoextendpercent: <number> # percentage of the autoextend profile
```

And some xfs dedicated roles
```yaml
---
lvnames:
  ...
  create: true
  filesystem2: xfs # will format the logical volume using xfs
```

```yaml
---
lvnames:
  ...
  mntp: /var/lib/docker
  mount2: true # will mount the xfs file system
```

Limitation: this role isn't idempotent: if you execute it twice it will create the thinpool a second time (but don't be a blocker)

Dependencies
------------

As said, [mrlesmithjr.ansible-manage-lvm](https://github.com/mrlesmithjr/ansible-manage-lvm)

Example Playbook
----------------

See the [vars declared](https://github.com/OsgiliathEnterprise/ansible-manage-lvm-plus/blob/master/molecule/default/molecule.yml) on the molecule test, as well as [their impact](https://github.com/OsgiliathEnterprise/ansible-manage-lvm-plus/blob/master/molecule/default/tests/test_default.py) 

License
-------

[Apache-2](https://www.apache.org/licenses/LICENSE-2.0)

Author Information
------------------

* Twitter [@tcharl](https://twitter.com/Tcharl)
* Github [@tcharl](https://github.com/Tcharl)
* LinkedIn [Charlie Mordant](https://www.linkedin.com/in/charlie-mordant-51796a97/)