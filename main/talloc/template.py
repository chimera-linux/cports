pkgname = "talloc"
pkgver = "2.3.3"
pkgrel = 0
build_style = "waf"
configure_script = "buildtools/bin/waf"
configure_args = [
    "--disable-rpath", "--disable-rpath-install",
    "--builtin-libraries=replace", "--bundled-libraries=NONE",
]
hostmakedepends = [
    "pkgconf", "python", "gettext-tiny", "docbook-xsl-nons", "xsltproc",
]
makedepends = [
    "python-devel", "gettext-tiny-devel",
]
pkgdesc = "Hierarchical pool based memory allocator with destructors"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-3.0-or-later"
url = "https://talloc.samba.org"
source = f"https://download.samba.org/pub/{pkgname}/{pkgname}-{pkgver}.tar.gz"
sha256 = "6be95b2368bd0af1c4cd7a88146eb6ceea18e46c3ffc9330bf6262b40d1d8aaa"
options = ["!cross"]

@subpackage("talloc-devel")
def _devel(self):
    return self.default_devel()

@subpackage("libpytalloc-util")
def _devel(self):
    self.pkgdesc = f"{pkgdesc} (Python utility library)"

    return ["usr/lib/libpytalloc-util.so.*"]

@subpackage("talloc-python")
def _devel(self):
    self.pkgdesc = f"{pkgdesc} (Python bindings)"

    return ["usr/lib/python*"]
