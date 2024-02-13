pkgname = "tdb"
pkgver = "1.4.10"
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
    "xsltproc",
]
makedepends = ["python-devel", "gettext-devel"]
pkgdesc = "Simple database API similar to gdbm"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-3.0-or-later"
url = "https://tdb.samba.org"
source = f"https://download.samba.org/pub/{pkgname}/{pkgname}-{pkgver}.tar.gz"
sha256 = "02338e33c16c21c9e29571cef523e76b2b708636254f6f30c6cf195d48c62daf"
# we don't want their makefile
env = {"PYTHONHASHSEED": "1", "WAF_MAKE": "1"}
# FIXME cfi
hardening = ["vis", "!cfi"]
options = ["!cross", "linkundefver"]


@subpackage("tdb-devel")
def _devel(self):
    return self.default_devel()


@subpackage("tdb-progs")
def _progs(self):
    return self.default_progs()


@subpackage("tdb-python")
def _python(self):
    self.pkgdesc = f"{pkgdesc} (Python bindings)"
    self.depends += ["python"]

    return ["usr/lib/python*"]
