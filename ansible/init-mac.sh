#!/usr/bin/env bash

brew cask install vagrant
brew install ansible
brew install yamllint
brew install flake8
brew install python3
brew link --overwrite python
pip3 install ansible-lint
pip3 install molecule
pip3 install 'molecule-vagrant'
pip3 install paramiko
. init-virtualbox.sh





