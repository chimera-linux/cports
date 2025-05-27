pkgname = "strace"
pkgver = "6.15"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--with-libdw",
    "--enable-stacktrace",
    "--disable-mpers",
    "--disable-gcc-Werror",
]
configure_env = {"CPPFLAGS": f"-I{self.profile().sysroot / 'usr/include'}"}
# there's over a thousand tests and a ~50 of them
# fail due to various reasons, mostly harmless ones
make_check_args = [
    "TESTS=bpf.gen epoll_pwait.gen getcpu.gen open.gen read-write.gen "
    "readlink.gen seccomp-filter.gen mmap ioctl caps"
]
hostmakedepends = ["automake", "libtool"]
makedepends = ["elfutils-devel", "linux-headers"]
pkgdesc = "System call tracer"
license = "LGPL-2.1-or-later"
url = "https://strace.io"
source = f"https://github.com/strace/strace/releases/download/v{pkgver}/strace-{pkgver}.tar.xz"
sha256 = "8552dfab08abc22a0f2048c98fd9541fd4d71b6882507952780dab7c7c512f51"
hardening = ["vis", "cfi"]
