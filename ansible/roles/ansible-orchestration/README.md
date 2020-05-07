Orchestration
=========

* Galaxy: [![Ansible Galaxy](https://img.shields.io/badge/galaxy-tcharl.ansible_orchestration-660198.svg?style=flat)](https://galaxy.ansible.com/tcharl/ansible_users)
* Lint, Tests & requirements: ![Molecule](https://github.com/OsgiliathEnterprise/ansible-orchestration/workflows/Molecule/badge.svg)
* Chat: [![Join the chat at https://gitter.im/OsgiliathEnterprise/platform](https://badges.gitter.im/OsgiliathEnterprise/platform.svg)](https://gitter.im/OsgiliathEnterprise/platform?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)


Simple wrapper over [Minikube instalation role from gatsign](https://github.com/gantsign/ansible_role_minikube)
In addition, configures docker as a prerequisite using [the ansible_containerization role](https://github.com/OsgiliathEnterprise/ansible-containerization)

Requirements
------------

Nothing

Role Variables
--------------

Same as the ones from the original role

Dependencies
------------

* [Minikube instalation role from gatsign](https://github.com/gantsign/ansible_role_minikube)

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: username.rolename, x: 42 }

License
-------

[Apache-2](https://www.apache.org/licenses/LICENSE-2.0)

Author Information
------------------

* Twitter [@tcharl](https://twitter.com/Tcharl)
* Github [@tcharl](https://github.com/Tcharl)
* LinkedIn [Charlie Mordant](https://www.linkedin.com/in/charlie-mordant-51796a97/)
