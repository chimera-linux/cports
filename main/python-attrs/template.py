pkgname = "python-attrs"
pkgver = "21.2.0"
pkgrel = 0
build_style = "python_module"
hostmakedepends = ["python-setuptools"]
checkdepends = ["python-pytest"] # and other stuff, but does not matter
depends = ["python"]
pkgdesc = "Attributes without boilerplate"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://attrs.readthedocs.io"
source = f"$(PYPI_SITE)/a/attrs/attrs-{pkgver}.tar.gz"
sha256 = "ef6aaac3ca6cd92904cdd0d83f629a15f18053ec84e6432106f7a4d04ae4f5fb"
# dependency of pytest
options = ["!check", "lto"]

def post_install(self):
    self.install_license("LICENSE")
