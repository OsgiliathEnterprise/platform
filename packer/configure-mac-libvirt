#!/usr/bin/env bash

echo "As a prerequisite, you've got to install brew package manager and hashicorp packer"
. ./platform-properties.sh
xcode-select --install
sudo mkdir /usr/local/sbin
sudo chown -R $(whoami):admin /usr/local/sbin
brew install libiconv gcc libvirt vnc-server libxml2

if ! grep -q 'LDFLAGS="-L/usr/local/opt/libxml2/lib $LDFLAGS"' ~/.bash_profile; then
echo 'export LDFLAGS="-L/usr/local/opt/libxml2/lib $LDFLAGS"' >> ~/.bash_profile
fi
if ! grep -q 'CPPFLAGS="-I/usr/local/opt/libxml2/include $CPPFLAGS"' ~/.bash_profile; then
echo 'export CPPFLAGS="-I/usr/local/opt/libxml2/include $CPPFLAGS"' >> ~/.bash_profile
fi
if ! grep -q 'PKG_CONFIG_PATH="/usr/local/opt/libxml2/lib/pkgconfig $PKG_CONFIG_PATH"' ~/.bash_profile; then
echo 'export PKG_CONFIG_PATH="/usr/local/opt/libxml2/lib/pkgconfig $PKG_CONFIG_PATH"' >> ~/.bash_profile
fi
if ! grep -q 'PATH="/usr/local/opt/openssl@1.1/bin:$PATH"' ~/.bash_profile; then
echo 'export PATH="/usr/local/opt/openssl@1.1/bin:$PATH"' >> ~/.bash_profile
fi

if ! grep -q 'LDFLAGS="-L/usr/local/opt/openssl@1.1/lib $LDFLAGS"' ~/.bash_profile; then
echo 'export LDFLAGS="-L/usr/local/opt/openssl@1.1/lib $LDFLAGS"' >> ~/.bash_profile
fi
if ! grep -q 'CPPFLAGS="-I/usr/local/opt/openssl@1.1/include $CPPFLAGS"' ~/.bash_profile; then
echo 'export CPPFLAGS="-I/usr/local/opt/openssl@1.1/include $CPPFLAGS"' >> ~/.bash_profile
fi
if ! grep -q 'PKG_CONFIG_PATH="/usr/local/opt/openssl@1.1/lib/pkgconfig $PKG_CONFIG_PATH"' ~/.bash_profile; then
echo 'export PKG_CONFIG_PATH="/usr/local/opt/openssl@1.1/lib/pkgconfig $PKG_CONFIG_PATH"'
fi
CONFIGURE_ARGS='with-ldflags=-L/opt/vagrant/embedded/lib with-libvirt-include=/usr/local/include/libvirt with-libvirt-lib=/usr/local/lib' GEM_HOME=~/.vagrant.d/gems GEM_PATH=$GEM_HOME:/opt/vagrant/embedded/gems PATH=/opt/vagrant/embedded/bin:$PATH vagrant plugin install vagrant-libvirt
brew link libvirt
brew link qemu
sudo brew services start libvirt
sudo mkdir /var/run/libvirt
sudo ln -s /usr/local/var/run/libvirt/libvirt-sock /var/run/libvirt/libvirt-sock
sudo chown -R $(whoami):admin /var/run/libvirt
sudo mkdir /var/lib/libvirt
sudo mkdir /var/lib/libvirt/images
sudo chown -R $(whoami):admin /var/lib/libvirt

if ! grep -q '"type": "qemu","use_default_display": true, "display": "none", "accelerator": "hvf",' bento/packer_templates/$distroversion/$distro.json; then
  sed -i 's/"type": "qemu"/"type": "qemu","use_default_display": true, "display": "none", "accelerator": "hvf"/g' metamorphosis.txt
fi

echo "you should also start qemu default pool: virsh # pool-start default"

