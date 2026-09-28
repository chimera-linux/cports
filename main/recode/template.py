pkgname = "recode"
pkgver = "3.7.15"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = [
    "automake",
    "bison",
    "flex",
    "gettext-devel",
    "libtool",
    "libtool-devel",
    "python",
    "texinfo",
]
checkdepends = [
    "python-cython",
    "python-devel",
    "python-setuptools",
]
pkgdesc = "Charset converter tool and library"
license = "GPL-3.0-or-later AND LGPL-3.0-only"
url = "https://github.com/rrthomas/recode"
source = f"{url}/releases/download/v{pkgver}/recode-{pkgver}.tar.gz"
sha256 = "f590407fc51badb351973fc1333ee33111f05ec83a8f954fd8cf0c5e30439806"


@subpackage("recode-devel")
def _(self):
    return self.default_devel()
