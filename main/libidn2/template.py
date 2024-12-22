pkgname = "libidn2"
pkgver = "2.3.7"
pkgrel = 1
build_style = "gnu_configure"
# defines this to nothing and yields #if invalid syntax for some reason
make_build_args = ["GNULIBHEADERS_OVERRIDE_WINT_T=0"]
hostmakedepends = [
    "automake",
    "gettext-devel",
    "gtk-doc-tools",
    "libtool",
    "pkgconf",
]
makedepends = ["libunistring-devel"]
pkgdesc = "Internationalized string handling library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-3.0-or-later AND GPL-3.0-or-later"
url = "https://www.gnu.org/software/libidn#libidn2"
source = f"$(GNU_SITE)/libidn/libidn2-{pkgver}.tar.gz"
sha256 = "4c21a791b610b9519b9d0e12b8097bf2f359b12f8dd92647611a929e6bfd7d64"


@subpackage("libidn2-devel")
def _(self):
    return self.default_devel(
        extra=[
            "usr/share/info",
        ]
    )


@subpackage("libidn2-progs")
def _(self):
    return self.default_progs()
