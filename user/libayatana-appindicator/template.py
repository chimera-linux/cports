pkgname = "libayatana-appindicator"
pkgver = "0.6.0"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DENABLE_TESTS=ON", "-DENABLE_BINDINGS_MONO=OFF"]
# racey
make_check_args = ["-j1"]
hostmakedepends = [
    "cmake",
    "gobject-introspection",
    "ninja",
    "pkgconf",
    "vala",
]
makedepends = [
    "glib-devel",
    "gtk+3-devel",
    "libayatana-indicator-devel",
    "libdbusmenu-devel",
]
checkdepends = ["dbus-test-runner", "xserver-xorg-xvfb"]
pkgdesc = "Ayatana App Indicators Shared Library"
license = "GPL-3.0-only AND (LGPL-3.0-only OR LGPL-2.1-only)"
url = "https://github.com/AyatanaIndicators/libayatana-appindicator"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "23be92ad8eb9625ce93b23b14f82f3cf88a4970c31d48581945ddfbac0441d06"
options = ["!cross"]


@subpackage("libayatana-appindicator-devel")
def _(self):
    return self.default_devel()
