pkgname = "iproute2"
pkgver = "6.3.0"
pkgrel = 0
build_style = "configure"
configure_env = {"CC": "clang"}
make_cmd = "gmake"
make_install_args = ["SBINDIR=/usr/bin"]
hostmakedepends = ["pkgconf", "gmake", "perl", "flex", "bison"]
makedepends = [
    "libfl-devel-static",
    "libmnl-devel",
    "libxtables-devel",
    "linux-headers",
]
pkgdesc = "IP routing utilities"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-only"
url = "https://wiki.linuxfoundation.org/networking/iproute2"
source = f"$(KERNEL_SITE)/utils/net/{pkgname}/{pkgname}-{pkgver}.tar.xz"
sha256 = "dfb2a98db96e7a653cffc6693335a1a466e29a34b6ac528be48f35e1d2766732"
hardening = ["vis", "cfi"]


def do_check(self):
    self.make.invoke(None, ["-C", "testsuite"])


def post_install(self):
    self.rm(self.destdir / "usr/share/man/man3", recursive=True)
