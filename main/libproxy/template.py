pkgname = "libproxy"
pkgver = "0.5.6"
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
sha256 = "68cb4548143e843826a35e024dba8ced92117c0982c2cc9a4c8247e32d259603"
# FIXME int (glib-networking tests fail)
hardening = ["!int"]


@subpackage("libproxy-devel")
def _devel(self):
    return self.default_devel()


@subpackage("libproxy-progs")
def _progs(self):
    return self.default_progs()
