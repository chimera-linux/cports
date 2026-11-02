pkgname = "cjs"
pkgver = "140.1"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dskip_dbus_tests=true",
    "-Dskip_gtk_tests=true",
    "-Dinstalled_tests=false",
    "-Dprofiler=disabled",
    "-Db_ndebug=true",
]
hostmakedepends = [
    "glib-devel",
    "gobject-introspection",
    "meson",
    "pkgconf",
]
makedepends = [
    "cairo-devel",
    "dbus-devel",
    "glib-devel",
    "libedit-readline-devel",
    "mozjs140-devel",
]
checkdepends = ["bash", "gobject-introspection-freedesktop", "gtk+3"]
pkgdesc = "Cinnamon JavaScript interpreter"
license = "MIT OR LGPL-2.0-or-later"
url = "https://projects.linuxmint.com/cinnamon"
source = f"https://github.com/linuxmint/cjs/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "1e223ce6229a7dc926b5ec3ee42040f6848e466ab51eb36c415c283b0b03098c"
options = ["!cross"]


def post_install(self):
    self.install_license("COPYING")
    # seemingly ignores the configure arg
    self.uninstall("usr/lib/installed-tests")


@subpackage("cjs-devel")
def _(self):
    return self.default_devel()
