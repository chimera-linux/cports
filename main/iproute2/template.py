pkgname = "iproute2"
pkgver = "5.19.0"
pkgrel = 0
build_style = "configure"
configure_env = {"CC": "clang"}
make_cmd = "gmake"
make_install_args = ["SBINDIR=/usr/bin"]
hostmakedepends = ["pkgconf", "gmake", "perl", "flex", "bison"]
makedepends = ["libfl-devel-static", "libmnl-devel", "linux-headers"]
pkgdesc = "IP routing utilities"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-only"
url = "https://wiki.linuxfoundation.org/networking/iproute2"
source = f"$(KERNEL_SITE)/utils/net/{pkgname}/{pkgname}-{pkgver}.tar.xz"
sha256 = "26b7a34d6a7fd2f7a42e2b39c5a90cb61bac522d1096067ffeb195e5693d7791"

def do_check(self):
    self.make.invoke(None, ["-C", "testsuite"])

def post_install(self):
    self.rm(self.destdir / "usr/share/man/man3", recursive = True)
