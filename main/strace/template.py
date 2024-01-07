pkgname = "strace"
pkgver = "6.6"
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
source = f"https://github.com/{pkgname}/{pkgname}/releases/download/v{pkgver}/{pkgname}-{pkgver}.tar.xz"
sha256 = "421b4186c06b705163e64dc85f271ebdcf67660af8667283147d5e859fc8a96c"
# FIXME int (breaks)
hardening = ["vis", "cfi", "!int"]
# something's weird and it gets stuck
options = ["!check"]
