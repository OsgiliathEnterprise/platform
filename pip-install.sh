#!/bin/bash
pip freeze | xargs pip uninstall -y
pip install ansible-compat==0.5.0 ansible-lint six yamllint pytest-testinfra molecule molecule-vagrant= ansible netaddr python-vagrant flake8 jmespath molecule-docker