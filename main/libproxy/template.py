pkgname = "libproxy"
pkgver = "0.5.12"
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
license = "LGPL-2.1-or-later"
url = "http://libproxy.github.io/libproxy"
source = (
    f"https://github.com/libproxy/libproxy/archive/refs/tags/{pkgver}.tar.gz"
)
sha256 = "a1fa55991998b80a567450a9e84382421a7176a84446c95caaa8b72cf09fa86f"
# FIXME int (glib-networking tests fail)
hardening = ["!int"]


@subpackage("libproxy-devel")
def _(self):
    return self.default_devel()


@subpackage("libproxy-progs")
def _(self):
    return self.default_progs()
