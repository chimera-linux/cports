pkgname = "blueman"
pkgver = "2.4.1"
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
sha256 = "89a8cd453152c8cabbb63ad91432c68263dec15cd17f1ea14d56aec24cf25949"
# TODO
options = ["!check"]
