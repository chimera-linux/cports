pkgname = "python-dbus-fast"
pkgver = "2.32.0"
pkgrel = 0
build_style = "python_pep517"
make_check_wrapper = ["dbus-run-session"]
hostmakedepends = [
    "python-build",
    "python-cython",
    "python-installer",
    "python-poetry-core",
    "python-setuptools",
]
makedepends = [
    "python-devel",
]
depends = ["python"]
checkdepends = ["dbus", "python-pytest-asyncio", "python-pytest-timeout"]
pkgdesc = "DBus library for python"
maintainer = "Gnarwhal <git.aspect893@passmail.net>"
license = "MIT"
url = "https://pypi.org/project/dbus-fast"
source = f"https://github.com/Bluetooth-Devices/dbus-fast/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "084e32b1eea578ca2c891470a75a36b1f9017a879b3bccc03f74c602e4fe0a27"


def post_install(self):
    self.install_license("LICENSE")
