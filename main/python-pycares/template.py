pkgname = "python-pycares"
pkgver = "4.6.0"
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
license = "MIT"
url = "https://github.com/saghul/pycares"
source = f"$(PYPI_SITE)/p/pycares/pycares-{pkgver}.tar.gz"
sha256 = "b8a004b18a7465ac9400216bc3fad9d9966007af1ee32f4412d2b3a94e33456e"
# tests requires internet access
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
