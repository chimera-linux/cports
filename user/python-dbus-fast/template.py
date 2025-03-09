pkgname = "python-dbus-fast"
pkgver = "2.39.3"
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
license = "MIT"
url = "https://pypi.org/project/dbus-fast"
source = f"https://github.com/Bluetooth-Devices/dbus-fast/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "f6828324dc42d261671f591d78f9d03a68333a290b60fff4b6ec64a2655b1a56"


def post_install(self):
    self.install_license("LICENSE")
