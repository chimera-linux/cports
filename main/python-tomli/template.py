pkgname = "python-tomli"
pkgver = "2.1.0"
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
sha256 = "28acaee6066d53256a2351ad5dc9003ba25d43578b4177c421de0ece71caa103"


def post_install(self):
    self.install_license("LICENSE")
