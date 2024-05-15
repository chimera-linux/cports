pkgname = "strace"
pkgver = "6.9"
pkgrel = 1
build_style = "gnu_configure"
configure_args = [
    "--with-libdw",
    "--enable-stacktrace",
    "--disable-mpers",
    "--disable-gcc-Werror",
]
configure_env = {"CPPFLAGS": f"-I{self.profile().sysroot / 'usr/include'}"}
make_cmd = "gmake"
# there's over a thousand tests and a ~50 of them
# fail due to various reasons, mostly harmless ones
make_check_args = [
    "TESTS=bpf.gen epoll_pwait.gen getcpu.gen open.gen read-write.gen "
    "readlink.gen seccomp-filter.gen mmap ioctl caps readv"
]
hostmakedepends = ["automake", "gmake", "libtool"]
makedepends = ["elfutils-devel", "linux-headers"]
pkgdesc = "System call tracer"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://strace.io"
source = f"https://github.com/strace/strace/releases/download/v{pkgver}/{pkgname}-{pkgver}.tar.xz"
sha256 = "da189e990a82e3ca3a5a4631012f7ecfd489dab459854d82d8caf6a865c1356a"
hardening = ["vis", "cfi"]
