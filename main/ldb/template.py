pkgname = "ldb"
pkgver = "2.8.0"
pkgrel = 1
build_style = "waf"
configure_script = "buildtools/bin/waf"
configure_args = [
    "--disable-rpath",
    "--disable-rpath-install",
    "--builtin-libraries=replace",
    "--bundled-libraries=NONE",
    "--with-modulesdir=/usr/lib/ldb/modules",
    "--without-ldb-lmdb",  # don't depend on shit software
]
hostmakedepends = [
    "pkgconf",
    "python",
    "gettext",
    "docbook-xsl-nons",
    "xsltproc",
    "tevent-python",
    "tdb-python",
]
makedepends = [
    "python-devel",
    "cmocka-devel",
    "talloc-devel",
    "tdb-devel",
    "tevent-devel",
    "popt-devel",
    "gettext-devel",
]
pkgdesc = "LDAP-like database"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-3.0-or-later"
url = "https://www.samba.org/ldb"
source = f"https://download.samba.org/pub/{pkgname}/{pkgname}-{pkgver}.tar.gz"
sha256 = "358dca10fcd27207ac857a0d7f435a46dbc6cd1f7c10dbb840c1931bf1965f08"
env = {"PYTHONHASHSEED": "1"}
options = ["!cross", "linkundefver"]


@subpackage("ldb-devel")
def _devel(self):
    return self.default_devel()


@subpackage("libpyldb-util")
def _util(self):
    self.pkgdesc = f"{pkgdesc} (Python utility library)"

    return ["usr/lib/libpyldb-util.so.*"]


@subpackage("ldb-python")
def _python(self):
    self.pkgdesc = f"{pkgdesc} (Python bindings)"
    self.depends += ["python"]

    return ["usr/lib/python*"]


@subpackage("ldb-progs")
def _progs(self):
    return self.default_progs()
