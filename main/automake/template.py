pkgname = "automake"
pkgver = "1.17"
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
sha256 = "8920c1fc411e13b90bf704ef9db6f29d540e76d232cb3b2c9f4dc4cc599bd990"
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
