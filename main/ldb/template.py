pkgname = "ldb"
pkgver = "2.9.1"
pkgrel = 0
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
source = f"https://download.samba.org/pub/ldb/ldb-{pkgver}.tar.gz"
sha256 = "c95e4dc32dea8864b79899ee340c9fdf28b486f464bbc38ba99151a08b493f9b"
env = {"PYTHONHASHSEED": "1"}
# check sometimes hangs
options = ["!cross", "linkundefver"]


if self.profile().arch == "ppc64":
    options += ["!check"]


@subpackage("ldb-devel")
def _devel(self):
    return self.default_devel()


@subpackage("libpyldb-util")
def _util(self):
    self.subdesc = "Python utility library"

    return ["usr/lib/libpyldb-util.so.*"]


@subpackage("ldb-python")
def _python(self):
    self.subdesc = "Python bindings"
    self.depends += ["python"]

    return ["usr/lib/python*"]


@subpackage("ldb-progs")
def _progs(self):
    return self.default_progs()
