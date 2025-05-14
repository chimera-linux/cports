pkgname = "python-cairo"
pkgver = "1.28.0"
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
license = "LGPL-2.1-or-later OR MPL-1.1"
url = "https://pycairo.readthedocs.io"
source = f"https://github.com/pygobject/pycairo/releases/download/v{pkgver}/pycairo-{pkgver}.tar.gz"
sha256 = "26ec5c6126781eb167089a123919f87baa2740da2cca9098be8b3a6b91cc5fbc"


@subpackage("python-cairo-devel")
def _(self):
    self.depends += [self.parent, "python-devel"]

    return self.default_devel()
