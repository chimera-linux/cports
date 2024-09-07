pkgname = "python-cairo"
pkgver = "1.27.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "meson",
    "pkgconf",
]
makedepends = ["cairo-devel", "python-devel"]
checkdepends = ["python-pytest"]
depends = ["python"]
pkgdesc = "Python bindings for the Cairo graphics library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later OR MPL-1.1"
url = "https://pycairo.readthedocs.io"
source = f"https://github.com/pygobject/pycairo/releases/download/v{pkgver}/pycairo-{pkgver}.tar.gz"
sha256 = "5cb21e7a00a2afcafea7f14390235be33497a2cce53a98a19389492a60628430"


@subpackage("python-cairo-devel")
def _(self):
    self.depends += [self.parent, "python-devel"]

    return self.default_devel()
