pkgname = "libidn2"
pkgver = "2.3.4"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["gettext-devel", "pkgconf"]
makedepends = ["libunistring-devel"]
pkgdesc = "Internationalized string handling library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-3.0-or-later AND GPL-3.0-or-later"
url = "https://www.gnu.org/software/libidn#libidn2"
source = f"$(GNU_SITE)/libidn/{pkgname}-{pkgver}.tar.gz"
sha256 = "93caba72b4e051d1f8d4f5a076ab63c99b77faee019b72b9783b267986dbb45f"
hardening = ["vis", "cfi"]


@subpackage("libidn2-devel")
def _devel(self):
    return self.default_devel(
        extra=[
            "usr/share/info",
        ]
    )


@subpackage("libidn2-progs")
def _progs(self):
    return self.default_progs()


configure_gen = []
