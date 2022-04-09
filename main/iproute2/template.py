pkgname = "iproute2"
pkgver = "5.17.0"
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
sha256 = "6e384f1b42c75e1a9daac57866da37dcff909090ba86eb25a6e764da7893660e"

def do_check(self):
    self.make.invoke(None, ["-C", "testsuite"])

def post_install(self):
    self.rm(self.destdir / "usr/share/man/man3", recursive = True)
