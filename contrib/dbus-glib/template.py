pkgname = "dbus-glib"
pkgver = "0.112"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--disable-static",
    "--disable-bash-completion",
]
make_cmd = "gmake"
hostmakedepends = ["pkgconf", "gmake"]
makedepends = ["glib-devel", "dbus-devel"]
checkdepends = ["dbus", "python"]
depends = ["dbus"]
pkgdesc = "GLib bindings for DBus (deprecated)"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://www.freedesktop.org/wiki/Software/DBusBindings"
source = (
    f"http://dbus.freedesktop.org/releases/{pkgname}/{pkgname}-{pkgver}.tar.gz"
)
sha256 = "7d550dccdfcd286e33895501829ed971eeb65c614e73aadb4a08aeef719b143a"
options = ["!cross"]


@subpackage("dbus-glib-devel")
def _devel(self):
    return self.default_devel()


configure_gen = []
