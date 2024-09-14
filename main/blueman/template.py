pkgname = "blueman"
pkgver = "2.4.3"
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
source = f"https://github.com/blueman-project/blueman/releases/download/{pkgver}/blueman-{pkgver}.tar.xz"
sha256 = "bdfc49909742cb79288f8a11d6f666b75c2713b91c085e6d0dd329434793fe85"
# TODO
options = ["!check"]


def post_install(self):
    self.uninstall("usr/lib/systemd/user")
    self.uninstall("usr/lib/systemd/system")
