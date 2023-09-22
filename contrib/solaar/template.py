pkgname = "solaar"
pkgver = "1.1.10"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-setuptools",
    "python-build",
    "python-wheel",
    "python-installer",
]
depends = [
    "python-evdev",
    "python-pyudev",
    "python-psutil",
    "python-pyyaml",
    "python-xlib",
    "python-gobject",
    "python-dbus",
]
pkgdesc = "Device manager for Logitech devices"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://pwr-solaar.github.io/Solaar"
source = (
    f"https://github.com/pwr-Solaar/Solaar/archive/refs/tags/{pkgver}.tar.gz"
)
sha256 = "40887b508e4cfc753e5c2e82caa4af7f057cadad4a32f238f9aef898b8ccfb2c"
# no tests
options = ["!check"]


def post_install(self):
    self.install_dir("usr/lib/udev/rules.d")
    self.mv(
        self.destdir
        / "usr/share/solaar/udev-rules.d/42-logitech-unify-permissions.rules",
        self.destdir / "usr/lib/udev/rules.d",
    )
