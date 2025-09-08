pkgname = "libwpd"
pkgver = "0.10.3"
pkgrel = 7
build_style = "gnu_configure"
make_dir = "."
hostmakedepends = [
    "automake",
    "pkgconf",
    "slibtool",
]
makedepends = ["librevenge-devel", "boost-devel"]
pkgdesc = "Library for importing WordPerfect documents"
license = "MPL-2.0 OR LGPL-2.1-or-later"
url = "https://libwpd.sourceforge.net"
source = f"$(SOURCEFORGE_SITE)/libwpd/libwpd-{pkgver}.tar.xz"
sha256 = "2465b0b662fdc5d4e3bebcdc9a79027713fb629ca2bff04a3c9251fdec42dd09"


@subpackage("libwpd-progs")
def _(self):
    return self.default_progs()


@subpackage("libwpd-devel")
def _(self):
    return self.default_devel()
