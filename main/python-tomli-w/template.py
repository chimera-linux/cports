pkgname = "python-tomli-w"
pkgver = "1.1.0"
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
sha256 = "bf9a4ccddb0b03cf2538479ac2210827ef5d5ff77de576f07147042b903bfb32"


def post_install(self):
    self.install_license("LICENSE")
