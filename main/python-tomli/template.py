pkgname = "python-tomli"
pkgver = "2.0.2"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = ["python-build", "python-flit_core", "python-installer"]
depends = ["python"]
checkdepends = ["python-pytest"]
pkgdesc = "TOML parser for Python"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://github.com/hukkin/tomli"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "a3a652f16bf326ba763ada67169165daf87ff9c465e21ad8264f2657beaf5264"


def post_install(self):
    self.install_license("LICENSE")
