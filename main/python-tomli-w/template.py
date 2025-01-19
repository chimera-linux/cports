pkgname = "python-tomli-w"
pkgver = "1.2.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-flit_core",
    "python-installer",
]
makedepends = ["python-pytest"]
checkdepends = ["python-tomli"]
depends = ["python"]
pkgdesc = "TOML writer for Python"
maintainer = "ttyyls <contact@behri.org>"
license = "MIT"
url = "https://github.com/hukkin/tomli-w"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "3b423098831faf35be897c5018c93e7c67eabf95d3359e1d5e97e5a4c0265ace"


def post_install(self):
    self.install_license("LICENSE")
