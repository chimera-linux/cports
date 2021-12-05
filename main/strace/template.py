pkgname = "strace"
pkgver = "5.14"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--without-libunwind", "--disable-mpers", "--disable-gcc-Werror",
    "--disable-dependency-tracking",
]
configure_env = {
    "CPPFLAGS": f"-I{self.profile().sysroot / 'usr/include'}"
}
make_cmd = "gmake"
# there's over a thousand tests and a ~50 of them
# fail due to various reasons, mostly harmless ones
make_check_args = [
    "TESTS=bpf.gen epoll_pwait.gen getcpu.gen open.gen read-write.gen "
    "readlink.gen seccomp-filter.gen mmap ioctl caps readv"
]
hostmakedepends = ["gmake"]
makedepends = ["linux-headers"]
pkgdesc = "System call tracer"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://strace.io"
source = f"https://github.com/{pkgname}/{pkgname}/releases/download/v{pkgver}/{pkgname}-{pkgver}.tar.xz"
sha256 = "901bee6db5e17debad4530dd9ffb4dc9a96c4a656edbe1c3141b7cb307b11e73"
