pkgname = "libkkc-data"
pkgver = "0.2.7"
_libkkc = "0.3.5"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = [
    "automake",
    "python",
    "python-marisa",
]
pkgdesc = "Data for libkkc"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "https://github.com/ueno/libkkc"
source = f"{url}/releases/download/v{_libkkc}/libkkc-data-{pkgver}.tar.xz"
sha256 = "9e678755a030043da68e37a4049aa296c296869ff1fb9e6c70026b2541595b99"
