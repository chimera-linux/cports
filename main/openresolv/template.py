pkgname = "openresolv"
pkgver = "3.13.2"
pkgrel = 1
build_style = "gnu_configure"
configure_args = ["--libexecdir=/usr/libexec/resolvconf"]
make_dir = "."
pkgdesc = "Management framework for resolv.conf"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
url = "https://roy.marples.name/projects/openresolv"
source = f"https://github.com/NetworkConfiguration/openresolv/releases/download/v{pkgver}/{pkgname}-{pkgver}.tar.xz"
sha256 = "36b5bcbe257a940c884f0d74321a47407baabab9e265e38859851c8311f6f0b0"
hardening = ["vis", "cfi"]
# no test suite
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
    # rename
    self.rename("usr/bin/resolvconf", "resolvconf-openresolv")
    self.rename("usr/share/man/man8/resolvconf.8", "resolvconf-openresolv.8")


configure_gen = []
