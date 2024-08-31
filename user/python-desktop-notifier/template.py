pkgname = "python-desktop-notifier"
pkgver = "6.0.0"
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
maintainer = "Gnarwhal <git.aspect893@passmail.net>"
license = "MIT"
url = "https://pypi.org/project/desktop-notifier"
source = f"https://github.com/samschott/desktop-notifier/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "b0604b1b92e6b5d74d943c43a125769a8258cc82347590637001b65eff1e1ba9"
# no org.freedesktop.Notifications in chroot
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
