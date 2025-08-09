pkgname = "python-desktop-notifier"
pkgver = "6.2.0"
pkgrel = 0
build_style = "python_pep517"
make_check_wrapper = ["dbus-run-session"]
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
]
depends = ["python-bidict", "python-dbus-fast", "python-packaging"]
checkdepends = ["dbus", "python-pytest-asyncio", *depends]
pkgdesc = "Cross-platform desktop notification library"
license = "MIT"
url = "https://pypi.org/project/desktop-notifier"
source = f"https://github.com/samschott/desktop-notifier/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "8953ff5e6cb1415e8d770cd84f4b35d912d2f935711c59abc3a0317925a5dbe4"
# no org.freedesktop.Notifications in chroot
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
