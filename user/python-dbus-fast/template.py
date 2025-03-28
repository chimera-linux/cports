pkgname = "python-dbus-fast"
pkgver = "2.43.0"
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
sha256 = "3461c0b8353cea40a6bc93c00cf8e28a4a5075fcb4b57b33eb2e51108b61b043"


def post_prepare(self):
    # Requires pytest_codspeed
    self.rm(self.srcdir / "tests/benchmarks", recursive=True)


def post_install(self):
    self.install_license("LICENSE")
