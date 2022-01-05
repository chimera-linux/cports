pkgname = "libproxy"
pkgver = "0.4.17"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DWITH_GNOME2=OFF",
    "-DWITH_MOZJS=OFF",
    "-DWITH_NM=OFF",
    "-DWITH_PERL=OFF",
    "-DWITH_WEBKIT=OFF",
    "-DWITH_GNOME3=ON",
    "-DWITH_KDE=ON",
    "-DWITH_PYTHON3=ON",
]
hostmakedepends = ["cmake", "ninja", "pkgconf", "python", "glib-devel"]
makedepends = ["libglib-devel", "zlib-devel"]
pkgdesc = "Automatic proxy configuration management library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "http://libproxy.github.io/libproxy"
source = f"https://github.com/{pkgname}/{pkgname}/releases/download/{pkgver}/{pkgname}-{pkgver}.tar.xz"
sha256 = "bc89f842f654ee1985a31c0ba56dc7e2ce8044a0264ddca84e650f46cd7f8b05"

@subpackage("libproxy-devel")
def _devel(self):
    return self.default_devel()

@subpackage("libproxy-progs")
def _progs(self):
    return self.default_progs()

@subpackage("libproxy-python")
def _python(self):
    self.pkgdesc = f"{pkgdesc} (Python bindings)"
    self.depends += [f"{pkgname}={pkgver}-r{pkgrel}", "python"]

    return ["usr/lib/python*"]
