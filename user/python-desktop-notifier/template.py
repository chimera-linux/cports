pkgname = "python-desktop-notifier"
pkgver = "6.1.1"
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
sha256 = "60b1eef6edb645ce48eb89fa8ef955e6c0aa34787808247587acc16c281fe871"
# no org.freedesktop.Notifications in chroot
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
