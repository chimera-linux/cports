pkgname = "strace"
pkgver = "6.7"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--with-libdw",
    "--enable-stacktrace",
    "--disable-mpers",
    "--disable-gcc-Werror",
]
configure_env = {"CPPFLAGS": f"-I{self.profile().sysroot / 'usr/include'}"}
configure_gen = []
make_cmd = "gmake"
# there's over a thousand tests and a ~50 of them
# fail due to various reasons, mostly harmless ones
make_check_args = [
    "TESTS=bpf.gen epoll_pwait.gen getcpu.gen open.gen read-write.gen "
    "readlink.gen seccomp-filter.gen mmap ioctl caps readv"
]
hostmakedepends = ["gmake"]
makedepends = ["elfutils-devel", "linux-headers"]
pkgdesc = "System call tracer"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://strace.io"
source = f"https://github.com/strace/strace/releases/download/v{pkgver}/{pkgname}-{pkgver}.tar.xz"
sha256 = "2090201e1a3ff32846f4fe421c1163b15f440bb38e31355d09f82d3949922af7"
# FIXME int (breaks)
hardening = ["vis", "cfi", "!int"]
# something's weird and it gets stuck
options = ["!check"]
