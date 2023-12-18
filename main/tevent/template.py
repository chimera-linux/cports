pkgname = "tevent"
pkgver = "0.16.0"
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
makedepends = [
    "python-devel",
    "talloc-devel",
    "cmocka-devel",
    "gettext-devel",
]
pkgdesc = "Event system based on talloc"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-3.0-or-later"
url = "https://tevent.samba.org"
source = f"https://download.samba.org/pub/{pkgname}/{pkgname}-{pkgver}.tar.gz"
sha256 = "1aa58f21017ed8c2f606ae84aa7e795b5439edd4dd5f68f1a388a7d6fb40f682"
# we don't want their makefile
env = {"PYTHONHASHSEED": "1", "WAF_MAKE": "1"}
# FIXME check fails in some envs
options = ["!cross", "!check", "linkundefver"]


@subpackage("tevent-devel")
def _devel(self):
    return self.default_devel()


@subpackage("tevent-python")
def _python(self):
    self.pkgdesc = f"{pkgdesc} (Python bindings)"

    return ["usr/lib/python*"]
