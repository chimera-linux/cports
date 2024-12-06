pkgname = "python-tomli"
pkgver = "2.2.1"
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
sha256 = "3af7c4b571d1ccddaba020c558da0ce5b5e24edc830e478a903d82dc2d9013ae"


def post_install(self):
    self.install_license("LICENSE")
