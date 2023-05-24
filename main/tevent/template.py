pkgname = "tevent"
pkgver = "0.14.1"
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
    "gettext-tiny",
    "docbook-xsl-nons",
    "xsltproc",
]
makedepends = [
    "python-devel",
    "talloc-devel",
    "cmocka-devel",
    "gettext-tiny-devel",
]
pkgdesc = "Event system based on talloc"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-3.0-or-later"
url = "https://tevent.samba.org"
source = f"https://download.samba.org/pub/{pkgname}/{pkgname}-{pkgver}.tar.gz"
sha256 = "ef85fcaa80ffd2351036ba4b347630fef2a1ac3da964a7f1820466bad03cd00d"
# we don't want their makefile
env = {"PYTHONHASHSEED": "1", "WAF_MAKE": "1"}
options = ["!cross"]


@subpackage("tevent-devel")
def _devel(self):
    return self.default_devel()


@subpackage("tevent-python")
def _devel(self):
    self.pkgdesc = f"{pkgdesc} (Python bindings)"

    return ["usr/lib/python*"]
