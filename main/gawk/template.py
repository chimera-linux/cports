pkgname = "gawk"
pkgver = "5.1.1"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--with-readline"]
makedepends = ["libedit-readline-devel"]
pkgdesc = "GNU awk utility"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "http://www.gnu.org/software/gawk"
source = f"$(GNU_SITE)/gawk/gawk-{pkgver}.tar.xz"
sha256 = "d87629386e894bbea11a5e00515fc909dc9b7249529dad9e6a3a2c77085f7ea2"

def post_install(self):
    # hardlinks + we don't want to conflict with awk
    (self.destdir / "usr/bin/awk").unlink()
    (self.destdir / "usr/bin/gawk").unlink()
    self.install_link(f"gawk-{pkgver}", "usr/bin/gawk")
