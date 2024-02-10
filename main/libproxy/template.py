pkgname = "libproxy"
pkgver = "0.5.4"
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
    "zlib-devel",
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
sha256 = "a6e2220349b2025de9b6d9d7f8bb347bf0c728f02a921761ad5f9f66c7436de9"
# FIXME int (glib-networking tests fail)
hardening = ["!int"]


@subpackage("libproxy-devel")
def _devel(self):
    return self.default_devel()


@subpackage("libproxy-progs")
def _progs(self):
    return self.default_progs()
