Orchestration Client
=========

* Galaxy: [![Ansible Galaxy](https://img.shields.io/badge/galaxy-tcharl.ansible_orchestration_cli-660198.svg?style=flat)](https://galaxy.ansible.com/tcharl/ansible_orchestration_cli)
* Lint & requirements: ![Molecule](https://github.com/OsgiliathEnterprise/ansible-orchestration-cli/workflows/Molecule/badge.svg)
* Tests: [![Build Status](https://travis-ci.com/OsgiliathEnterprise/ansible-orchestration-cli.svg?branch=master)](https://travis-ci.com/OsgiliathEnterprise/ansible-orchestration-cli)
* Chat: [![Join the chat at https://gitter.im/OsgiliathEnterprise/platform](https://badges.gitter.im/OsgiliathEnterprise/platform.svg)](https://gitter.im/OsgiliathEnterprise/platform?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

A cli for the [ansible orchestration role](https://github.com/OsgiliathEnterprise/ansible-orchestration).

* It will run some kubernetes commands (kubectl apply -f ...) on master nodes.
* It will install helm

Requirements
------------

A kubernetes installed, a client cert, a key and a CA on the master node.

Role Variables
--------------

As an example, see the [Molecule test vars](./molecule/default/converge.yml) and the [default variables](./defaults/main.yml)

Dependencies
------------

* See [requirements](./requirements.yml)
* See [requirements-collections](./requirements-collections.yml)

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts:
       - kube_master
      roles:
         - { role: tcharl.ansible_orchestration_cli }
    - hosts:
       - kube_node
      roles:
         - { role: tcharl.ansible_orchestration_cli }

License
-------

[Apache-2](https://www.apache.org/licenses/LICENSE-2.0)

Author Information
------------------

* Twitter [@tcharl](https://twitter.com/Tcharl)
* Github [@tcharl](https://github.com/Tcharl)
* LinkedIn [Charlie Mordant](https://www.linkedin.com/in/charlie-mordant-51796a97/)
