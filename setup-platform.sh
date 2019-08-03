#!/bin/sh

echo "As a prerequisite, run the install script related to your distro"

vagrant plugin update
rm -rf ~/.vagrant.d/boxes #remove vagrant box cache

. ./platform-properties.sh
cd "$(dirname ${BASH_SOURCE[0]})/packer/bento"
git pull upstream master
cd ../..
cd "$(dirname ${BASH_SOURCE[0]})/packer/bento/packer_templates/$distro"
packer build -var "box_basename=$distroversion" -only=virtualbox-iso $distroversion.json

echo export platform_root=$CWD >> ~/.bash_profile
source ~/.bash_profile