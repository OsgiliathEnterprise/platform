 Osgiliath Platform
 =========
| Repo | Lint status | Tests status | Galaxy url |
|-----------|-------------|--------------|------------|
| [Platform](https://github.com/OsgiliathEnterprise/platform)|![Publish documentation](https://github.com/OsgiliathEnterprise/platform/workflows/Publish%20documentation/badge.svg)|![Publish documentation](https://github.com/OsgiliathEnterprise/platform/workflows/Publish%20documentation/badge.svg)||
| [Containerization](https://github.com/OsgiliathEnterprise/ansible-containerization)|![Molecule](https://github.com/OsgiliathEnterprise/ansible-containerization/workflows/Molecule/badge.svg)|[![Build Status](https://travis-ci.com/OsgiliathEnterprise/ansible-containerization.svg?branch=master)](https://travis-ci.com/OsgiliathEnterprise/ansible-containerization)|[![Ansible Galaxy](https://img.shields.io/badge/galaxy-tcharl.ansible_containerization-660198.svg?style=flat)](https://galaxy.ansible.com/tcharl/ansible_containerization)|
| [Routing](https://github.com/OsgiliathEnterprise/ansible-routing)|![Molecule](https://github.com/OsgiliathEnterprise/ansible-routing/workflows/Molecule/badge.svg)|[![Build Status](https://travis-ci.com/OsgiliathEnterprise/ansible-routing.svg?branch=master)](https://travis-ci.com/OsgiliathEnterprise/ansible-routing)|[![Ansible Galaxy](https://img.shields.io/badge/galaxy-tcharl.ansible_routing-660198.svg?style=flat)](https://galaxy.ansible.com/tcharl/ansible_routing)|
| [SecureHost](https://github.com/OsgiliathEnterprise/ansible-securehost)|![Molecule](https://www.travis-ci.com/OsgiliathEnterprise/ansible-securehost.svg?branch=master)|![Molecule](https://github.com/OsgiliathEnterprise/ansible-securehost/workflows/Molecule/badge.svg)|[![Ansible Galaxy](https://img.shields.io/badge/galaxy-tcharl.ansible_securehost-660198.svg?style=flat)](https://galaxy.ansible.com/tcharl/ansible_securehost)|
| [Users](https://github.com/OsgiliathEnterprise/ansible-users)|![Molecule](https://github.com/OsgiliathEnterprise/ansible-users/workflows/Molecule/badge.svg)|![Molecule](https://github.com/OsgiliathEnterprise/ansible-users/workflows/Molecule/badge.svg)|[![Ansible Galaxy](https://img.shields.io/badge/galaxy-tcharl.ansible_users-660198.svg?style=flat)](https://galaxy.ansible.com/tcharl/ansible_users)|
| [Virtualization](https://github.com/OsgiliathEnterprise/ansible-virtualization)|![Molecule](https://github.com/OsgiliathEnterprise/ansible-virtualization/workflows/Molecule/badge.svg)|[![Build Status](https://travis-ci.com/OsgiliathEnterprise/ansible-virtualization.svg?branch=master)](https://travis-ci.com/OsgiliathEnterprise/ansible-virtualization)|[![Ansible Galaxy](https://img.shields.io/badge/galaxy-tcharl.ansible_virtualization-660198.svg?style=flat)](https://galaxy.ansible.com/tcharl/ansible_virtualization)|
| [Virt-guest](https://github.com/OsgiliathEnterprise/ansible-virtualization-guest)|![Molecule](https://github.com/OsgiliathEnterprise/ansible-virtualization-guest/workflows/Molecule/badge.svg)|[![Build Status](https://travis-ci.com/OsgiliathEnterprise/ansible-virtualization-guest.svg?branch=master)](https://travis-ci.com/OsgiliathEnterprise/ansible-virtualization-guest)|[![Ansible Galaxy](https://img.shields.io/badge/galaxy-tcharl.ansible_virtualization_guest-660198.svg?style=flat)](https://galaxy.ansible.com/tcharl/ansible_virtualization_guest)|
| [Volumes](https://github.com/OsgiliathEnterprise/ansible-volumes)|![Molecule](https://github.com/OsgiliathEnterprise/ansible-volumes/workflows/Molecule/badge.svg)|[![Build Status](https://travis-ci.com/OsgiliathEnterprise/ansible-volumes.svg?branch=master)](https://travis-ci.com/OsgiliathEnterprise/ansible-volumes)|[![Ansible Galaxy](https://img.shields.io/badge/galaxy-tcharl.ansible_volumes-660198.svg?style=flat)](https://galaxy.ansible.com/tcharl/ansible_volumes)|
| [Nameserver](https://github.com/OsgiliathEnterprise/ansible-nameserver)|![Molecule](https://github.com/OsgiliathEnterprise/ansible-nameserver/workflows/Molecule/badge.svg)|[![Build Status](https://travis-ci.com/OsgiliathEnterprise/ansible-nameserver.svg?branch=master)](https://travis-ci.com/OsgiliathEnterprise/ansible-nameserver)|[![Ansible Galaxy](https://img.shields.io/badge/galaxy-tcharl.ansible_nameserver-660198.svg?style=flat)](https://galaxy.ansible.com/tcharl/ansible_nameserver)|
| [Orchestration](https://github.com/OsgiliathEnterprise/ansible-orchestration)|![Molecule](https://github.com/OsgiliathEnterprise/ansible-orchestration/workflows/Molecule/badge.svg)|[![Build Status](https://travis-ci.com/OsgiliathEnterprise/ansible-orchestration.svg?branch=master)](https://travis-ci.com/OsgiliathEnterprise/ansible-orchestration)|[![Ansible Galaxy](https://img.shields.io/badge/galaxy-tcharl.ansible-orchestration-660198.svg?style=flat)](https://galaxy.ansible.com/tcharl/ansible_orchestration)|
| [Container registry](https://github.com/OsgiliathEnterprise/ansible-container-registry)|![Molecule](https://github.com/OsgiliathEnterprise/ansible-container-registry/workflows/Molecule/badge.svg)|[![Build Status](https://travis-ci.com/OsgiliathEnterprise/ansible-container-registry.svg?branch=master)](https://travis-ci.com/OsgiliathEnterprise/ansible-container-registry)|[![Ansible Galaxy](https://img.shields.io/badge/galaxy-tcharl.ansible-container-registry-660198.svg?style=flat)](https://galaxy.ansible.com/tcharl/ansible_container_registry)|


[![Join the chat at https://gitter.im/OsgiliathEnterprise/platform](https://badges.gitter.im/OsgiliathEnterprise/platform.svg)](https://gitter.im/OsgiliathEnterprise/platform?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

 # What is it?
 
 Is it a bunch of infrastructure scripts (Packer, Ansible, Terraform, Dockerfiles, Kubernetes Helm Charts) that will ease the setup of a full OSS Information System (including people management, mails, HR, ERP, EMD, Engineering, ...) targeting cloud and on premise.

As of now, it focuses on setting up a fully secured production platform (with kubernetes) that can scale from 1 to inifinite.
Technically speaking, the stack is dealing with the following technologies:
 * LVM
 * NFS
 * FreeIPA (including Kerberos, PKI, internal DNS, company LDAP)
 * Libvirt and KVM (to simulate multi-server with VMs)
 * Nginx-proxy & letencrypt
 * Kubernetes
 * And of course other low level security & host stack: Firewalld, Fail2ban, /etc/hosts, ...
 
 * Want a new business relative integration ? Feel free to [propose a new category](https://github.com/OsgiliathEnterprise/platform/issues/new?labels=Status%3A+Untriaged&template=CATEGORY_TEMPLATE.md)
 * Want to propose a new solution answering to a business need? [Tell us your recommendation](https://github.com/OsgiliathEnterprise/platform/issues/new?labels=Status%3A+Untriaged&template=SOLUTION_TEMPLATE.md)
 
 Solution proposal are submitted by the community and choosed democratically via votes on tickets, then integrated in the platform.
 The platform delivery goal is to provide a one (or just a little bit more) click solution to deploy the overall integrated stack for your company.
 
# Documentation
 
 Checkout the [reference documentation](https://osgiliathenterprise.github.io/platform/reference/toc.html) for more information.

# Status
 
This project is looking for active contributors and committers, feel free [to join us and produce anything you'll find useful](https://github.com/OsgiliathEnterprise/platform/blob/master/CONTRIBUTING.md)