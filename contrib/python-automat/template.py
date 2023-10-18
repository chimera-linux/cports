pkgname = "python-automat"
pkgver = "22.10.0"
pkgrel = 0
build_style = "python_module"
hostmakedepends = ["python-setuptools", "python-setuptools_scm", "python-wheel"]
depends = ["python-setuptools", "python-attrs", "python-six"]
checkdepends = ["python-pytest", "python-graphviz"] + list(depends)
pkgdesc = "Finite state machines for Python"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://github.com/glyph/Automat"
source = f"$(PYPI_SITE)/A/Automat/Automat-{pkgver}.tar.gz"
sha256 = "e56beb84edad19dcc11d30e8d9b895f75deeb5ef5e96b84a467066b3b84bb04e"
# unpackaged checkdepends
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
