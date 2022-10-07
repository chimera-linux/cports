pkgname = "ldb"
pkgver = "2.6.1"
pkgrel = 0
build_style = "waf"
configure_script = "buildtools/bin/waf"
configure_args = [
    "--disable-rpath", "--disable-rpath-install",
    "--builtin-libraries=replace", "--bundled-libraries=NONE",
    "--with-modulesdir=/usr/lib/ldb/modules",
]
hostmakedepends = [
    "pkgconf", "python", "gettext-tiny", "docbook-xsl-nons", "xsltproc",
    "tevent-python", "tdb-python",
]
makedepends = [
    "python-devel", "cmocka-devel", "talloc-devel", "tdb-devel",
    "tevent-devel", "popt-devel", "lmdb-devel", "gettext-tiny-devel",
]
pkgdesc = "LDAP-like database"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-3.0-or-later"
url = "https://www.samba.org/ldb"
source = f"https://download.samba.org/pub/{pkgname}/{pkgname}-{pkgver}.tar.gz"
sha256 = "467403f77df86782c3965bb175440baa2ed751a9feb9560194bd8c06bf1736c9"
# we don't want their makefile
env = {"PYTHONHASHSEED": "1", "WAF_MAKE": "1"}
options = ["!cross"]

@subpackage("ldb-devel")
def _devel(self):
    return self.default_devel()

@subpackage("libpyldb-util")
def _devel(self):
    self.pkgdesc = f"{pkgdesc} (Python utility library)"

    return ["usr/lib/libpyldb-util.so.*"]

@subpackage("ldb-python")
def _devel(self):
    self.pkgdesc = f"{pkgdesc} (Python bindings)"

    return ["usr/lib/python*"]

@subpackage("ldb-progs")
def _progs(self):
    return self.default_progs()
