pkgname = "recode"
pkgver = "3.7.14"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = [
    "automake",
    "bison",
    "flex",
    "gettext-devel",
    "libtool-devel",
    "libtool",
    "python",
    "texinfo",
]
checkdepends = [
    "python-cython",
    "python-devel",
]
pkgdesc = "Charset converter tool and library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later AND LGPL-3.0-only"
url = "https://github.com/rrthomas/recode"
source = f"{url}/releases/download/v{pkgver}/recode-{pkgver}.tar.gz"
sha256 = "786aafd544851a2b13b0a377eac1500f820ce62615ccc2e630b501e7743b9f33"
# tests need cython + python devel, does not build with our versions
options = ["!check"]


@subpackage("recode-devel")
def _(self):
    return self.default_devel()
