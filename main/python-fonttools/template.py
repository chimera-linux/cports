pkgname = "python-fonttools"
pkgver = "4.51.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = ["python"]
checkdepends = ["python-pytest"]
pkgdesc = "Library to manipulate font files from Python"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT AND OFL-1.1 AND BSD-3-Clause AND Apache-2.0"
url = "https://github.com/fonttools/fonttools"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "85aa9cdf030dd82f28ca584a8814de265150b46bfc65067343a631773efa885a"


def post_install(self):
    self.install_license("LICENSE")
    self.install_license("LICENSE.external")
