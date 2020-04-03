Lvm-manager
=========

This role is an extension of the [most used lvm cookbook](https://github.com/mrlesmithjr/ansible-manage-lvm).
It add the ability to create thinpools

Role Variables
--------------

In addition to the [usual variables](https://github.com/mrlesmithjr/ansible-manage-lvm/blob/master/README.md), you can declare some more.
```
lvnames:
  ...
  metadata: <another lvname> # declares the metadata logical volume 
```

```
lvnames:
  ...
  autoextendtreshold: <number> # treshold of the autoextend profile
  autoextendpercent: <number> # percentage of the autoextend profile
```

Dependencies
------------

As said, mrlesmithjr.ansible-manage-lvm

Example Playbook
----------------

See the [vars declared](molecule/default/molecule.yml) on the molecule test, as well as [their impact](molecule/default/tests/test_default.py) 

License
-------

Apache-2

Author Information
------------------

Twitter [@tcharl](https://twitter.com/Tcharl)
Github [@tcharl](https://github.com/Tcharl)
LinkedIn [Charlie Mordant](https://www.linkedin.com/in/charlie-mordant-51796a97/)