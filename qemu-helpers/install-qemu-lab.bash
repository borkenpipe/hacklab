#!/bin/bash

SUDOINSTALL="sudo install -v "

if [ -r logger-support ] ; then source  logger-support ; else echo "I need logger-support. Quitting" ; fi

PREFIX="/opt/qemu-hacklab"

mkdir /tmp/hacklab.install.tmp
echo "\$HACKLABPATH=$PREFIX" > /tmp/hacklab.install.tmp/hacklab-paths

TARGETBIN="$PREFIX/bin/"
TARGETLIB="$PREFIX/lib/"

info "Installing qemu-lab-support"

TARGETDIRS="$TARGETBIN $TARGETLIB"
sudo mkdir -v $TARGETDIRS -p || fail "Couldn't created $TARGETDIRS"

$SUDOINSTALL -v bin/* $TARGETBIN
$SUDOINSTALL -v lib/* $TARGETBIN





