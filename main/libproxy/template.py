pkgname = "libproxy"
pkgver = "0.5.8"
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
    "meson",
    "pkgconf",
    "glib-devel",
    "gobject-introspection",
    "vala",
    "bash",
]
makedepends = [
    "glib-devel",
    "zlib-ng-compat-devel",
    "gsettings-desktop-schemas-devel",
    "duktape-devel",
]
pkgdesc = "Automatic proxy configuration management library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "http://libproxy.github.io/libproxy"
source = (
    f"https://github.com/libproxy/libproxy/archive/refs/tags/{pkgver}.tar.gz"
)
sha256 = "64e363855012175bf796b37cacddf7bc7e08af0bf406eea94b549ce207987d3e"
# FIXME int (glib-networking tests fail)
hardening = ["!int"]


@subpackage("libproxy-devel")
def _(self):
    return self.default_devel()


@subpackage("libproxy-progs")
def _(self):
    return self.default_progs()
