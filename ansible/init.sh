#!/usr/bin/env bash

vagrant plugin update
vagrant plugin install vagrant-persistent-storage

rm -rf ~/.vagrant.d/boxes #remove vagrant box cache

if [[ "$OSTYPE" == "linux-gnu" ]]; then
  echo "not implemented for linux, PR welcomed!"
elif [[ "$OSTYPE" == "darwin"* ]]; then
. ./init-mac.sh
fi

cd roles
git clone git@github.com:OsgiliathEnterprise/ansible-manage-lvm-plus.git