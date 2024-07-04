pkgname = "findutils"
pkgver = "4.10.0"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--program-prefix=g"]
hostmakedepends = [
    "automake",
    "gettext-devel",
    "texinfo",
]
pkgdesc = "GNU find utilities"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "http://www.gnu.org/software/findutils"
source = f"$(GNU_SITE)/{pkgname}/{pkgname}-{pkgver}.tar.xz"
sha256 = "1387e0b67ff247d2abde998f90dfbf70c1491391a59ddfecb8ae698789f0a4f5"
hardening = ["vis", "cfi"]


def post_install(self):
    # we don't want this
    self.uninstall("usr/bin/glocate")
    self.uninstall("usr/bin/gupdatedb")
    self.uninstall("usr/libexec")
    self.uninstall("usr/share/man/man1/glocate.1")
    self.uninstall("usr/share/man/man1/gupdatedb.1")
    self.uninstall("usr/share/man/man5")
