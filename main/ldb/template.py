pkgname = "ldb"
pkgver = "2.7.2"
pkgrel = 0
build_style = "waf"
configure_script = "buildtools/bin/waf"
configure_args = [
    "--disable-rpath", "--disable-rpath-install",
    "--builtin-libraries=replace", "--bundled-libraries=NONE",
    "--with-modulesdir=/usr/lib/ldb/modules",
    "--without-ldb-lmdb", # don't depend on shit software
]
hostmakedepends = [
    "pkgconf", "python", "gettext-tiny", "docbook-xsl-nons", "xsltproc",
    "tevent-python", "tdb-python",
]
makedepends = [
    "python-devel", "cmocka-devel", "talloc-devel", "tdb-devel",
    "tevent-devel", "popt-devel", "gettext-tiny-devel",
]
pkgdesc = "LDAP-like database"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-3.0-or-later"
url = "https://www.samba.org/ldb"
source = f"https://download.samba.org/pub/{pkgname}/{pkgname}-{pkgver}.tar.gz"
sha256 = "26ee72d647854e662d99643eb2b2d341655abf31f4990838d6650fb5cf9209c8"
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
    self.depends += ["python"]

    return ["usr/lib/python*"]

@subpackage("ldb-progs")
def _progs(self):
    return self.default_progs()
