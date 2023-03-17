pkgname = "gawk"
pkgver = "5.2.1"
pkgrel = 0
build_style = "gnu_configure"
# pma disables pie
configure_args = ["--with-readline", "--disable-pma"]
make_cmd = "gmake"
hostmakedepends = ["gmake"]
makedepends = ["libedit-readline-devel"]
pkgdesc = "GNU awk utility"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "http://www.gnu.org/software/gawk"
source = f"$(GNU_SITE)/gawk/gawk-{pkgver}.tar.xz"
sha256 = "673553b91f9e18cc5792ed51075df8d510c9040f550a6f74e09c9add243a7e4f"

def post_install(self):
    # hardlinks + we don't want to conflict with awk
    (self.destdir / "usr/bin/awk").unlink()
    (self.destdir / "usr/bin/gawk").unlink()
    self.install_link(f"gawk-{pkgver}", "usr/bin/gawk")
