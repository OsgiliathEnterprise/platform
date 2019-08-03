#!/usr/bin/env bash

echo "As a prerequisite, you've got to install brew package manager and hashicorp packer"

brew install cask
brew cask install vagrant
brew cask install virtualbox
brew install ansible
brew install yamllint
brew install flake8
pip install ansible-lint
pip install molecule
pip install 'molecule[vagrant]'
pip install paramiko