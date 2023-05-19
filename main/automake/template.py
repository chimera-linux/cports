pkgname = "automake"
pkgver = "1.16.5"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["perl", "autoconf"]
checkdepends = ["flex", "gettext-tiny-devel", "pkgconf"]
depends = ["perl", "autoconf"]
pkgdesc = "GNU Standards-compliant Makefile generator"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://www.gnu.org/software/automake"
source = f"$(GNU_SITE)/{pkgname}/{pkgname}-{pkgver}.tar.gz"
sha256 = "07bd24ad08a64bc17250ce09ec56e921d6343903943e99ccf63bbf0705e34605"
# flakey, a different set of tests fails every time
options = ["!check"]

def post_install(self):
    fp = self.destdir / "usr/bin/aclocal"
    fp.unlink()
    fp.symlink_to(f"aclocal-{pkgver[:-2]}")
    fp = self.destdir / "usr/bin/automake"
    fp.unlink()
    fp.symlink_to(f"automake-{pkgver[:-2]}")

configure_gen = []
