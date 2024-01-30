pkgname = "python-pycares"
pkgver = "4.4.0"
pkgrel = 0
build_style = "python_pep517"
make_build_env = {"PYCARES_USE_SYSTEM_LIB": "1"}
hostmakedepends = [
    "python-build",
    "python-cffi",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
makedepends = ["c-ares-devel", "python-devel"]
depends = ["python-cffi"]
pkgdesc = "Python bindings for c-ares"
maintainer = "miko <mikoxyzzz@gmail.com>"
license = "MIT"
url = "https://github.com/saghul/pycares"
source = f"$(PYPI_SITE)/p/pycares/pycares-{pkgver}.tar.gz"
sha256 = "f47579d508f2f56eddd16ce72045782ad3b1b3b678098699e2b6a1b30733e1c2"
# tests requires internet access
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
