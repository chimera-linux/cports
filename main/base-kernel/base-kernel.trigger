#!/bin/sh

[ -f /.cbuild_chroot_init ] && exit 0

/usr/lib/base-kernel/run-kernel-d || :
