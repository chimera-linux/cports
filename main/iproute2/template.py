pkgname = "iproute2"
pkgver = "5.15.0"
pkgrel = 0
build_style = "configure"
configure_env = {"CC": "clang"}
make_cmd = "gmake"
make_install_args = ["SBINDIR=/usr/bin"]
hostmakedepends = ["pkgconf", "gmake", "perl", "flex", "bison"]
# TODO: db implementation for arpd
makedepends = ["libfl-static", "libmnl-devel", "linux-headers"]
pkgdesc = "IP routing utilities"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-only"
url = "https://wiki.linuxfoundation.org/networking/iproute2"
source = f"$(KERNEL_SITE)/utils/net/{pkgname}/{pkgname}-{pkgver}.tar.xz"
sha256 = "38e3e4a5f9a7f5575c015027a10df097c149111eeb739993128e5b2b35b291ff"
options = ["lto"]

def do_check(self):
    self.make.invoke(None, ["-C", "testsuite"])

def post_install(self):
    self.rm(self.destdir / "usr/share/man/man3", recursive = True)
