pkgname = "tdb"
pkgver = "1.4.12"
pkgrel = 0
build_style = "waf"
configure_script = "buildtools/bin/waf"
configure_args = [
    "--disable-rpath",
    "--disable-rpath-install",
    "--builtin-libraries=replace",
    "--bundled-libraries=NONE",
]
hostmakedepends = [
    "pkgconf",
    "python",
    "gettext",
    "docbook-xsl-nons",
    "libxslt-progs",
]
makedepends = ["python-devel", "gettext-devel"]
pkgdesc = "Simple database API similar to gdbm"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-3.0-or-later"
url = "https://tdb.samba.org"
source = f"https://download.samba.org/pub/tdb/tdb-{pkgver}.tar.gz"
sha256 = "6ce4b27498812d09237ece65a0d6dfac0941610e709848ecb822aa241084cd7a"
# we don't want their makefile
env = {"PYTHONHASHSEED": "1", "WAF_MAKE": "1"}
hardening = ["vis", "!cfi"]
options = ["!cross", "linkundefver"]


@subpackage("tdb-devel")
def _(self):
    return self.default_devel()


@subpackage("tdb-progs")
def _(self):
    return self.default_progs()


@subpackage("tdb-python")
def _(self):
    self.subdesc = "Python bindings"
    self.depends += ["python"]

    return ["usr/lib/python*"]
