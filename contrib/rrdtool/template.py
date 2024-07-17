pkgname = "rrdtool"
pkgver = "1.8.0"
pkgrel = 2
build_style = "gnu_configure"
make_dir = "."
hostmakedepends = [
        "automake",
        "bash",
        "gettext-devel",
        "libtool",
        "pkgconf",
        "python-setuptools",
]
makedepends = ["glib-devel", "libxml2-devel", "pango-devel", "python-devel"]
pkgdesc = "Round Robin Database Tool"
maintainer = "yanchan09 <yan@omg.lol>"
license = "GPL-2.0-or-later AND custom:FLOSS-License-Exception"
url = "https://oss.oetiker.ch/rrdtool"
source = f"https://github.com/oetiker/rrdtool-1.x/releases/download/v{pkgver}/{pkgname}-{pkgver}.tar.gz"
sha256 = "bd37614137d7a8dc523359648eb2a81631a34fd91a82ed5581916a52c08433f4"

def post_install(self):
    self.install_license("LICENSE")
    self.install_license("COPYRIGHT")

@subpackage("librrd")
def _librrd(self):
    self.pkgdesc = "Manipulate time-series round-robin databases"

    return self.default_libs()

@subpackage("librrd-devel")
def _devel(self):
    self.depends += makedepends
    self.pkgdesc = "Manipulate time-series round-robin databases (development files)"

    return self.default_devel()

@subpackage(f"{pkgname}-python")
def _python(self):
    self.subdesc = "Python bindings"
    self.depends += ["python"]

    return ["usr/lib/python*", "usr/share/rrdtool/examples/*.py"]
