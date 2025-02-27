pkgname = "newt"
pkgver = "0.52.24"
pkgrel = 1
build_style = "gnu_configure"
# reconf breaks library soname stuff (???)
configure_gen = []
make_dir = "."
hostmakedepends = ["pkgconf", "python-devel"]
makedepends = ["python-devel", "slang-devel", "popt-devel"]
pkgdesc = "Library for color text mode, widget based user interfaces"
license = "LGPL-2.0-only"
url = "https://pagure.io/newt"
source = f"https://releases.pagure.org/newt/newt-{pkgver}.tar.gz"
sha256 = "5ded7e221f85f642521c49b1826c8de19845aa372baf5d630a51774b544fbdbb"
# no proper check target
options = ["!check"]


@subpackage("newt-devel")
def _(self):
    return self.default_devel()


@subpackage("newt-python")
def _(self):
    self.subdesc = "Python bindings"
    self.depends += ["python"]

    return ["usr/lib/python*"]
