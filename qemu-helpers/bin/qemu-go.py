#!/usr/bin/env python

import os, sys, re
import importlib

PREFIX="/opt/qemu-hacklab"
PREFIXBACKUP="."
LOGGER_MODULE_FILENAME="loggerSupport"
LOGGER_MODULE = os.path.join(PREFIX,LOGGER_MODULE_FILENAME)

directory, module_name = os.path.split(LOGGER_MODULE)
module_name = os.path.splitext(module_name)[0]
path = list(sys.path)
sys.path.insert(0, directory)
try:
    logmod = __import__(module_name)
finally:
    sys.path[:] = path # restore

def usage(msg=""):
    usageText = """
    usage: $0 options

    OPTIONS:
       -h      Show this message.
       -d      Debug messages on, implies verbose.
       -v      Verbose messages on.
       -a      Architecture to use.
       -r      Action to do [install|run]
       -b      Use the base directory where qemu files/disks are stored.
       -m      Macaddress to use for qemu VM.
       -i      Network interface to use.
       -c      First time init for vm store
    """
    print("%s\n%s" % (usageText, msg))

def main():
    print("SDF")
    logmod.info("YO DUDE")
    logmod.verbose("YO DUDE")
    logmod.debug("YO DUDE")
    logmod.debug_pause("YO DUDE")
    logmod.fail("YO DUDE")
    logmod.cleanup("DONT DO ME")
"""

if [ -z $HLUSER ] ; then
    HLUSER=$USER
fi
if [ -z $HLGROUP ] ; then
    HLGROUP=$GROUP
fi

MACADDR="52:54:00:12:34:11"
INTERFACE="tap0"
ARCH=""
ACTION=""
BASEDIR=""
INITVMDIR=""
while getopts “hdva:r:b:m:i:c” OPTION
do
    case $OPTION in
        h)
            usage
            exit 1
            ;;
        d)
            DEBUG="yes"
            VERBOSE="yes"
            ;;
        v)
            VERBOSE="yes"
            ;;
        a)
            ARCH=$OPTARG
            ;;
        r)
            ACTION=$OPTARG
            ;;
        b)
            BASEDIR=$OPTARG
            ;;
        m)
            MACADDR=$OPTARG
            ;;
        i)
            INTERFACE=$OPTARG
            ;;
        c)
            INITVMDIR="yes"
            ;;
        ?)
            usage
            exit
            ;;
    esac
done

chown_dir_to_target_install_user_group ()
{

    if [ ! -z $1 ] ; then
        TARGETDIR=$1
        sudo chown -Rv $HLUSER:$HLGROUP $TARGETDIR || fail "Expected chown to succeed"
    fi
    return 0
}

list_vms_dir ()
{
    verbose "Checking $HLDESTDISKDIR"
    ls -1 $HLDESTDISKDIR
}

init_vms_dir ()
{
    sudo mkdir -v $HLBASEINSTALL || fail "Couldn't create $HLBASEINSTALL"
    chown_dir_to_target_install_user_group $HLBASEINSTALL || fail "Couldn't set user:group ($HLUSER:$HLGROUP) on $HLBASEINSTALL"
    sudo mkdir -v $HLDESTDISKDIR -p || fail "Couldn't create $HLDESTDISKDIR"
    chown_dir_to_target_install_user_group $HLDESTDISKDIR || fail "Couldn't set user::group ($HLUSER:$HLGROUP) on $HLDESTDISKDIR"
    return 0
}

debug "Sourcing helper paths"

source qemu-helper-paths

if [ ! -z $INITVMDIR ] ; then
    init_vms_dir || fail "Failed to initialize"
fi

if [ -z $ARCH ] ; then
    list_vms_dir
    exit 0
fi

if [ -z $ARCH ] ; then usage ; fail "no ARCH specified" ; fi
if [ -z $ACTION ] ; then usage ; fail "no ACTION specified i.e., $0 ARCH [install|run]" ; fi

if [ -z $BASEDIR ] ; then info "Using $HLDESTDISKDIR for qemu disk store" && cd $HLDESTDISKDIR ; fi
if [ ! -z $BASEDIR ] ; then cd $BASEDIR || fail "Couldn't change directory to qemu disk store at: \"$BASEDIR\""; fi
if [ ! -d $ARCH ] ; then usage ; fail "Expected architecture directory \"$ARCH\" to exist in `pwd`" ; fi
cd $ARCH

QEMUBIN=`which qemu-system-$ARCH`
HARDDISK="debian_mips.qcow2-$ARCH"
KERNEL="vmlinux-2.6.32-5-4kc-malta-$ARCH"
INITRD="initrd.gz-$ARCH"

if [ ! -x $QEMUBIN ] ; then fail "no qemu binary $QEMUBIN" ; fi
if [ ! -r $HARDDISK ] ; then fail "no harddisk: $HARDDISK" ; fi
if [ ! -r $KERNEL ] ; then fail "no $KERNEL" ; fi
if [ ! -r $INITRD ] ; then fail "no $INITRD" ; fi

if [[ $ACTION == "install" ]] ; then
    echo qemu-system-$ARCH -hda $HARDDISK -kernel $KERNEL -initrd $INITRD -append "root=/dev/ram console=ttyS0" -nographic
    read -p"go?"
    qemu-system-$ARCH -hda $HARDDISK -kernel $KERNEL -initrd $INITRD -append "root=/dev/ram console=ttyS0" -nographic
elif [[ $ACTION == "run" ]] ; then
    sudo qemu-system-$ARCH \
            -hda $HARDDISK \
            -kernel $KERNEL \
            -append "root=/dev/sda1 console=ttyS0" \
            -nographic \
            -net nic,macaddr=$MACADDR \
            -net tap,ifname=$INTERFACE,script=no,downscript=no 
else
    usage
    echo "Give me an action like: $0 -a mipsel -r install"
fi

"""

if __name__ == "__main__":
    main()
