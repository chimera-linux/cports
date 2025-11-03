pkgname = "automake"
pkgver = "1.18.1"
pkgrel = 0
build_style = "gnu_configure"
# circle with itself
configure_gen = []
hostmakedepends = ["perl", "autoconf"]
checkdepends = ["flex", "gettext-devel", "pkgconf"]
depends = ["perl", "autoconf"]
pkgdesc = "GNU Standards-compliant Makefile generator"
license = "GPL-2.0-or-later"
url = "https://www.gnu.org/software/automake"
source = f"$(GNU_SITE)/automake/automake-{pkgver}.tar.xz"
sha256 = "168aa363278351b89af56684448f525a5bce5079d0b6842bd910fdd3f1646887"
# flakey, a different set of tests fails every time
options = ["!check"]


def post_install(self):
    # .patch suffix after second dot is omitted from the script version
    mver = ".".join(pkgver.split(".")[0:2])
    # remove hardlinks
    fp = self.destdir / "usr/bin/aclocal"
    fp.unlink()
    fp.symlink_to(f"aclocal-{mver}")
    fp = self.destdir / "usr/bin/automake"
    fp.unlink()
    fp.symlink_to(f"automake-{mver}")
