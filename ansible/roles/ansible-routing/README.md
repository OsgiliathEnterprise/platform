Routing
=========

* Galaxy: [![Ansible Galaxy](https://img.shields.io/badge/galaxy-tcharl.ansible_routing-660198.svg?style=flat)](https://galaxy.ansible.com/tcharl/ansible_routing)
* Lint: ![Molecule](https://github.com/OsgiliathEnterprise/ansible-routing/workflows/Molecule/badge.svg)
* Tests: [![Build Status](https://travis-ci.org/OsgiliathEnterprise/ansible-routing.svg?branch=master)](https://travis-ci.org/OsgiliathEnterprise/ansible-routing)
* Chat: [![Join the chat at https://gitter.im/OsgiliathEnterprise/platform](https://badges.gitter.im/OsgiliathEnterprise/platform.svg)](https://gitter.im/OsgiliathEnterprise/platform?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

This role let you configure simple port or port/IP redirections using firewalld masquerade

Requirements
------------

Ansible :-)

Role Variables
--------------

```
firewalld_zones:
  - name: public # optional
    nics:
      - eth0 # optional
    masquerade: true
    port_forward_rules:
      - port_forward_rule: ssh-to-guest
        family: ipv4 # optional
        from_port: 6752
        protocol: tcp # optional
        to_address: 192.168.1.10
        to_port: 22

```

License
-------


[Apache-2](https://www.apache.org/licenses/LICENSE-2.0)

Author Information
------------------

* Twitter [@tcharl](https://twitter.com/Tcharl)
* Github [@tcharl](https://github.com/Tcharl)
* LinkedIn [Charlie Mordant](https://www.linkedin.com/in/charlie-mordant-51796a97/)
