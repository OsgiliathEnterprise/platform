Nameserver
=========

* Galaxy: [![Ansible Galaxy](https://img.shields.io/badge/galaxy-tcharl.ansible_nameserver-660198.svg?style=flat)](https://galaxy.ansible.com/tcharl/ansible_nameserver)
* Lint,  & requirements: ![Molecule](https://github.com/OsgiliathEnterprise/ansible-nameserver/workflows/Molecule/badge.svg)
* Tests: [![Build Status](https://travis-ci.org/OsgiliathEnterprise/ansible-nameserver.svg?branch=master)](https://travis-ci.org/OsgiliathEnterprise/ansible-nameserver)
* Chat: [![Join the chat at https://gitter.im/OsgiliathEnterprise/platform](https://badges.gitter.im/OsgiliathEnterprise/platform.svg)](https://gitter.im/OsgiliathEnterprise/platform?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

Foir now, this role configures the hostname of the machine and add the entry in /etc/hosts

Requirements
------------

Unix machine :-)

Role Variables
--------------

```
hostname: "{{ inventory_hostname }}" # default
```

Dependencies
------------

  - name: tcharl.hostname
  - name: robertdebock.reboot
  - name: robertdebock.bootstrap
  - name: robertdebock.core_dependencies

License
-------


[Apache-2](https://www.apache.org/licenses/LICENSE-2.0)

Author Information
------------------

* Twitter [@tcharl](https://twitter.com/Tcharl)
* Github [@tcharl](https://github.com/Tcharl)
* LinkedIn [Charlie Mordant](https://www.linkedin.com/in/charlie-mordant-51796a97/)
