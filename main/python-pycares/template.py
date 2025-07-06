pkgname = "python-pycares"
pkgver = "4.9.0"
pkgrel = 0
build_style = "python_pep517"
make_build_env = {"PYCARES_USE_SYSTEM_LIB": "1"}
hostmakedepends = [
    "python-build",
    "python-cffi",
    "python-installer",
    "python-setuptools",
]
makedepends = ["c-ares-devel", "python-devel"]
depends = ["python-cffi"]
pkgdesc = "Python bindings for c-ares"
license = "MIT"
url = "https://github.com/saghul/pycares"
source = f"$(PYPI_SITE)/p/pycares/pycares-{pkgver}.tar.gz"
sha256 = "8ee484ddb23dbec4d88d14ed5b6d592c1960d2e93c385d5e52b6fad564d82395"
# tests requires internet access
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
