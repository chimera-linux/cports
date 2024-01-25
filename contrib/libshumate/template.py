pkgname = "libshumate"
pkgver = "1.1.2"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dgtk_doc=false"]
make_check_wrapper = ["weston-headless-run", "dbus-run-session"]
hostmakedepends = [
    "meson",
    "pkgconf",
]
makedepends = [
    "gtk4-devel",
    "libsoup-devel",
]
checkdepends = [
    "dbus",
    "weston",
]
pkgdesc = "GTK4 widgets for maps"
maintainer = "psykose <alice@ayaya.dev>"
license = "LGPL-2.1-or-later"
url = "https://gitlab.gnome.org/GNOME/libshumate"
source = f"$(GNOME_SITE)/libshumate/{pkgver[:pkgver.rfind('.')]}/libshumate-{pkgver}.tar.xz"
sha256 = "8f094f6e7e256ab192800516ff96617abeec2363b054aad6aeb17e0088c1fb2c"
# vis breaks symbols
hardening = ["!vis"]


@subpackage("libshumate-devel")
def _devel(self):
    return self.default_devel()
