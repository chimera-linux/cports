pkgname = "libplist"
pkgver = "2.4.0"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--disable-static"]  # prevent building python binding .a
hostmakedepends = ["pkgconf", "automake", "libtool", "python", "python-cython"]
makedepends = ["python-devel", "glib-devel", "libxml2-devel"]
pkgdesc = "Apple Property List library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-only"
url = "https://libimobiledevice.org"
source = f"https://github.com/libimobiledevice/libplist/releases/download/{pkgver}/{pkgname}-{pkgver}.tar.bz2"
sha256 = "3f5868ae15b117320c1ff5e71be53d29469d4696c4085f89db1975705781a7cd"
# FIXME int
hardening = ["!int"]
options = ["!cross"]


@subpackage("libplist++")
def _pp(self):
    self.pkgdesc = f"{pkgdesc} (C++ runtime library)"

    return ["usr/lib/libplist++*.so.*"]


@subpackage("libplist-python")
def _python(self):
    self.pkgdesc = f"{pkgdesc} (Python bindings)"

    return ["usr/lib/python3*"]


@subpackage("libplist-devel")
def _devel(self):
    return self.default_devel()


@subpackage("libplist-progs")
def _progs(self):
    return self.default_progs()
