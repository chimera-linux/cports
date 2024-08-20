pkgname = "libayatana-appindicator"
pkgver = "0.5.93"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DENABLE_TESTS=ON", "-DENABLE_BINDINGS_MONO=OFF"]
# racey
make_check_args = ["-j1"]
make_check_env = {"NO_AT_BRIDGE": "1"}
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
maintainer = "triallax <triallax@tutanota.com>"
license = "GPL-3.0-only AND (LGPL-3.0-only OR LGPL-2.1-only)"
url = "https://github.com/AyatanaIndicators/libayatana-appindicator"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "cbefed7a918a227bf71286246e237fcd3a9c8499b3eaac4897811a869409edf0"
options = ["linkundefver", "!cross"]


@subpackage("libayatana-appindicator-devel")
def _(self):
    return self.default_devel()
