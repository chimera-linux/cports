pkgname = "tdb"
pkgver = "1.4.15"
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
    "docbook-xsl-nons",
    "gettext",
    "libxslt-progs",
    "pkgconf",
    "python",
]
makedepends = ["python-devel", "gettext-devel"]
pkgdesc = "Simple database API similar to gdbm"
license = "LGPL-3.0-or-later"
url = "https://tdb.samba.org"
source = f"https://download.samba.org/pub/tdb/tdb-{pkgver}.tar.gz"
sha256 = "fba09d8df1f1b9072aeae8e78b2bd43c5afef20b2f6deefa633aa14a377a8dd2"
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
