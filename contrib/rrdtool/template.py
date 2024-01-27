pkgname = "rrdtool"
pkgver = "1.8.0"
pkgrel = 0
build_style = "gnu_configure"
make_dir = "."
hostmakedepends = [
    "automake",
    "bash",
    "gettext-devel",
    "groff",
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
    self.install_license("COPYRIGHT")


@subpackage(f"{pkgname}-devel")
def _devel(self):
    return self.default_devel()


@subpackage(f"{pkgname}-python")
def _python(self):
    self.pkgdesc = f"{pkgdesc} (Python bindings)"
    self.depends += ["python"]

    return ["usr/lib/python*", "usr/share/rrdtool/examples/*.py"]
