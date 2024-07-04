pkgname = "blueman"
pkgver = "2.4.2"
pkgrel = 0
build_style = "meson"
configure_args = ["-Druntime_deps_check=false"]
hostmakedepends = [
    "gettext",
    "glib",
    "meson",
    "pkgconf",
    "python",
    "python-cython",
]
makedepends = [
    "bluez-devel",
    "glib-devel",
    "linux-headers",
    "python-gobject-devel",
]
depends = [
    "bluez",
    "dbus",
    "gtk+3",
    "iproute2",
    "libnm",
    "libpulse",
    "python-cairo",
    "python-gobject",
]
checkdepends = ["python-dbusmock", "python-dbus"]
pkgdesc = "GTK Bluetooth Manager"
maintainer = "triallax <triallax@tutanota.com>"
license = "GPL-3.0-or-later"
url = "https://blueman-project.github.io/blueman"
source = f"https://github.com/blueman-project/blueman/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "01acfb0ab717ecc803ee10de4adacb161af998b69f12633e1885bea2ebd5fcd1"
# TODO
options = ["!check"]


def post_install(self):
    self.uninstall("usr/lib/systemd/user")
    self.uninstall("usr/lib/systemd/system")
