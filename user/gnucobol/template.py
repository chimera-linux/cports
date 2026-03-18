pkgname = "gnucobol"
pkgver = "3.2"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--without-db"]
make_dir = "."
hostmakedepends = ["automake", "gettext-devel", "libtool", "pkgconf"]
makedepends = [
    "gmp-devel",
    "json-c-devel",
    "libxml2-devel",
    "ncurses-devel",
]
checkdepends = ["curl", "perl"]
pkgdesc = "Free COBOL compiler"
license = "GPL-3.0-or-later"
url = "https://gnucobol.sourceforge.io"
source = f"$(GNU_SITE)/gnucobol/gnucobol-{pkgver}.tar.xz"
sha256 = "3bb48af46ced4779facf41fdc2ee60e4ccb86eaa99d010b36685315df39c2ee2"
options = ["!cross"]


@subpackage("gnucobol-static")
def _(self):
    return ["usr/lib/*.a"]


@subpackage("gnucobol-libs")
def _(self):
    return self.default_libs(extra=["usr/lib/gnucobol"])
