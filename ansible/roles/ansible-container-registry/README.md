Container registry
=========


* Galaxy: [![Ansible Galaxy](https://img.shields.io/badge/galaxy-tcharl.ansible_container-registry-660198.svg?style=flat)](https://galaxy.ansible.com/tcharl/ansible_container-registry)
* Lint & requirements: ![Molecule](https://github.com/OsgiliathEnterprise/ansible-container-registry/workflows/Molecule/badge.svg)
* Tests: [![Build Status](https://travis-ci.com/OsgiliathEnterprise/ansible-container-registry.svg?branch=master)](https://travis-ci.com/OsgiliathEnterprise/ansible-container-registry)
* Chat: [![Join the chat at https://gitter.im/OsgiliathEnterprise/platform](https://badges.gitter.im/OsgiliathEnterprise/platform.svg)](https://gitter.im/OsgiliathEnterprise/platform?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

This role is a fork of the original [andrewrothstein.docker-registry](https://github.com/andrewrothstein/ansible-docker-registry) role in order to add Let's encrypt configuration and exposing it via the jwilder/nginx-proxy docker container

Requirements
------------

You should first execute `./configure` first, which will download the requirements in siblings folders.
Then, configure your ansible.cfg file to include the requirements
`roles_path = ./roles:./roles/community


Molecule tests
--------------

You can execute `molecule test` to test the role. however it won't test letencrypt stuff

Role Variables
--------------

Only [dependencies variables](./defaults/molecule.yml) at all but those of the dependencies, and the dependent roles variables in addition like in [molecule tests](./molecule/default/converge.yml).

Dependencies
------------

As said
 * [tcharl ansible-containerization](https://github.com/tcharl/ansible-role-containerization)

Check the [requirements file](./requirements.yml)

Example Playbook
----------------

Be sure to get your DNS and a proper redirection to your server first
See the [vars declared](https://github.com/OsgiliathEnterprise/ansible-containerization/blob/master/molecule/default/molecule.yml) on the molecule test, as well as [their impact](https://github.com/OsgiliathEnterprise/ansible-containerization/blob/master/molecule/default/tests/test_default.py) 


License
-------

[Apache-2](https://www.apache.org/licenses/LICENSE-2.0)

Author Information
------------------

* Twitter [@tcharl](https://twitter.com/Tcharl)
* Github [@tcharl](https://github.com/Tcharl)
* LinkedIn [Charlie Mordant](https://www.linkedin.com/in/charlie-mordant-51796a97/)
