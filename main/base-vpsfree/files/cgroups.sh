#!/bin/sh

DINIT_SERVICE=cgroups

set -e

. ./early/scripts/common.sh

cgr_mode() {
    if grep -x "^[[:digit:]]:cpuset:/" /proc/1/cgroup > /dev/null; then
        echo "hybrid"
    else
        echo "unified"
    fi
}

cgr_hybrid() {
    echo "Mounting cgroups in hybrid layout..."

    local retval=0
    local name
    local mount_opts="nodev,noexec,nosuid"

    if ! mount -t tmpfs -o "$mount_opts" tmpfs /sys/fs/cgroup; then
        msg_warn "Unable to mount /sys/fs/cgroup"
        return 1
    fi

    cat /proc/1/cgroup | while read line; do
        controller=$(echo $line | cut -d ':' -f 2)

        case "$controller" in
            "")
                mkdir /sys/fs/cgroup/unified
                mount -n -t cgroup2 -o "$mount_opts" cgroup2 /sys/fs/cgroup/unified || retval=1
                ;;
            "name="*)
                name=$(echo $controller | cut -d '=' -f 2)
                mkdir "/sys/fs/cgroup/${name}"
                mount -n -t cgroup -o "none,$mount_opts,name=$name" \
                    cgroup "/sys/fs/cgroup/$name" || retval=1
                ;;
            *)
                mkdir "/sys/fs/cgroup/$controller"
                mount -n -t cgroup -o "$mount_opts,$controller" \
                    cgroup "/sys/fs/cgroup/$controller" || retval=1
                ;;
        esac
    done

    mount -o remount,ro tmpfs /sys/fs/cgroup

    return $retval
}

cgr_unified() {
    echo "Mounting cgroups in unified layout..."

    mkdir /sys/fs/cgroup/init.scope
    echo 1 > /sys/fs/cgroup/init.scope/cgroup.procs
}

case $(cgr_mode) in
    hybrid) cgr_hybrid ;;
    unified) cgr_unified ;;
    *) echo "unknown cgroup mode" ;;
esac
