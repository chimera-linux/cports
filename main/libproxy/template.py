pkgname = "libproxy"
pkgver = "0.5.9"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Ddocs=false",
    "-Dconfig-windows=false",
    "-Dconfig-osx=false",
    "-Dconfig-sysconfig=false",
    "-Dcurl=false",
]
hostmakedepends = [
    "bash",
    "glib-devel",
    "gobject-introspection",
    "meson",
    "pkgconf",
    "vala",
]
makedepends = [
    "duktape-devel",
    "glib-devel",
    "gsettings-desktop-schemas-devel",
    "zlib-ng-compat-devel",
]
pkgdesc = "Automatic proxy configuration management library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "http://libproxy.github.io/libproxy"
source = (
    f"https://github.com/libproxy/libproxy/archive/refs/tags/{pkgver}.tar.gz"
)
sha256 = "a1976c3ac4affedc17e6d40cf78c9d8eca6751520ea3cbbec1a8850f7ded1565"
# FIXME int (glib-networking tests fail)
hardening = ["!int"]


@subpackage("libproxy-devel")
def _(self):
    return self.default_devel()


@subpackage("libproxy-progs")
def _(self):
    return self.default_progs()
