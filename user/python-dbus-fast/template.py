pkgname = "python-dbus-fast"
pkgver = "2.24.2"
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
sha256 = "45ff3ff90183d013aa14edc1a3412d301cf3117d5f35b2fd10f478955fac3070"


def post_install(self):
    self.install_license("LICENSE")
