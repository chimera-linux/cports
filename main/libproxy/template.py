pkgname = "libproxy"
pkgver = "0.5.2"
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
    f"https://github.com/{pkgname}/{pkgname}/archive/refs/tags/{pkgver}.tar.gz"
)
sha256 = "7d75a2cf1c977056eb86f460daab0247d30e6a34e26ec755aab4de40cfd0a06d"
# FIXME int (glib-networking tests fail)
hardening = ["!int"]


@subpackage("libproxy-devel")
def _devel(self):
    return self.default_devel()


@subpackage("libproxy-progs")
def _progs(self):
    return self.default_progs()
