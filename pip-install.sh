#!/bin/bash
pip freeze | xargs pip uninstall -y
pip install ansible-lint six docker-py yamllint pytest-testinfra molecule molecule-vagrant==0.6.1 ansible netaddr python-vagrant flake8 jmespath