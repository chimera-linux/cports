pkgname = "newt"
pkgver = "0.52.24"
pkgrel = 1
build_style = "gnu_configure"
# reconf breaks library soname stuff (???)
configure_gen = []
make_cmd = "gmake"
make_dir = "."
hostmakedepends = ["gmake", "pkgconf", "python-devel"]
makedepends = ["python-devel", "slang-devel", "popt-devel"]
pkgdesc = "Library for color text mode, widget based user interfaces"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.0-only"
url = "https://pagure.io/newt"
source = f"https://pagure.io/releases/{pkgname}/{pkgname}-{pkgver}.tar.gz"
sha256 = "5ded7e221f85f642521c49b1826c8de19845aa372baf5d630a51774b544fbdbb"
# no proper check target
options = ["!check"]


@subpackage("newt-devel")
def _devel(self):
    return self.default_devel()


@subpackage("newt-python")
def _progs(self):
    self.pkgdesc = f"{pkgdesc} (Python bindings)"
    self.depends += ["python"]

    return ["usr/lib/python*"]
