#!/bin/sh

[ -f /.cbuild_chroot_init ] && exit 0

/usr/libexec/base-kernel/run-kernel-d || :
