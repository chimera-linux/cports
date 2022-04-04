pkgname = "tevent"
pkgver = "0.11.0"
pkgrel = 0
build_style = "waf"
configure_script = "buildtools/bin/waf"
configure_args = [
    "--disable-rpath", "--disable-rpath-install",
    "--builtin-libraries=replace", "--bundled-libraries=NONE",
]
hostmakedepends = [
    "pkgconf", "python", "gettext-tiny", "docbook-xsl-nons", "xsltproc",
]
makedepends = [
    "python-devel", "talloc-devel", "cmocka-devel", "gettext-tiny-devel",
]
pkgdesc = "Event system based on talloc"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-3.0-or-later"
url = "https://tevent.samba.org"
source = f"https://download.samba.org/pub/{pkgname}/{pkgname}-{pkgver}.tar.gz"
sha256 = "ee9a86c8e808aac2fe1e924eaa139ff7f0269d0e8e4fafa850ae5c7489bc82ba"
options = ["!cross"]

@subpackage("tevent-devel")
def _devel(self):
    return self.default_devel()

@subpackage("tevent-python")
def _devel(self):
    self.pkgdesc = f"{pkgdesc} (Python bindings)"

    return ["usr/lib/python*"]
