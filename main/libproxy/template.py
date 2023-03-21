pkgname = "libproxy"
pkgver = "0.4.18"
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
makedepends = ["glib-devel", "zlib-devel"]
pkgdesc = "Automatic proxy configuration management library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "http://libproxy.github.io/libproxy"
source = f"https://github.com/{pkgname}/{pkgname}/releases/download/{pkgver}/{pkgname}-{pkgver}.tar.xz"
sha256 = "69b5856e9ea42c38ac77e6b8c92ffc86a71d341fef74e77bef85f9cc6c47a4b1"
# FIXME int (glib-networking tests fail)
hardening = ["!int"]

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
