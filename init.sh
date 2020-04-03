#!/usr/bin/env bash

echo "As a prerequisite, run the install script related to your distro"

if ! grep -q "platform_root=" ~/.bash_profile; then
echo export platform_root=$(pwd) >> ~/.bash_profile
fi

if [[ "$OSTYPE" == "linux-gnu" ]]; then
        # do not work for now...
echo "not implemented for linux, PR welcomed!"
elif [[ "$OSTYPE" == "darwin"* ]]; then
. ./init-mac.sh
. ./packer/init.sh
fi

source ~/.bash_profile