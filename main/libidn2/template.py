pkgname = "libidn2"
pkgver = "2.3.3"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["gettext-tiny-devel", "pkgconf"]
makedepends = ["libunistring-devel"]
pkgdesc = "Internationalized string handling library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-3.0-or-later AND GPL-3.0-or-later"
url = "https://www.gnu.org/software/libidn#libidn2"
source = f"$(GNU_SITE)/libidn/{pkgname}-{pkgver}.tar.gz"
sha256 = "f3ac987522c00d33d44b323cae424e2cffcb4c63c6aa6cd1376edacbf1c36eb0"

@subpackage("libidn2-devel")
def _devel(self):
    return self.default_devel(extra = [
        "usr/share/info",
    ])

@subpackage("libidn2-progs")
def _progs(self):
    return self.default_progs()
