pkgname = "tdb"
pkgver = "1.4.6"
pkgrel = 0
build_style = "waf"
configure_script = "buildtools/bin/waf"
configure_args = [
    "--disable-rpath", "--disable-rpath-install",
    "--builtin-libraries=replace", "--bundled-libraries=NONE",
]
hostmakedepends = [
    "pkgconf", "python", "gettext-tiny", "docbook-xsl-nons"
]
makedepends = [
    "python-devel", "gettext-tiny-devel"
]
pkgdesc = "Simple database API similar to gdbm"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-3.0-or-later"
url = "https://tdb.samba.org"
source = f"https://download.samba.org/pub/{pkgname}/{pkgname}-{pkgver}.tar.gz"
sha256 = "d6892bd8befe04a77642a1dd56e4a879349bf1cf5b2c0bf5fb841061938def0b"
# FIXME check
options = ["!cross", "!check"]

@subpackage("tdb-devel")
def _devel(self):
    return self.default_devel()

@subpackage("tdb-progs")
def _devel(self):
    return self.default_progs()

@subpackage("tdb-python")
def _devel(self):
    self.pkgdesc = f"{pkgdesc} (Python bindings)"

    return ["usr/lib/python*"]
