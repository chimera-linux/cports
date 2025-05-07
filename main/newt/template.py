pkgname = "newt"
pkgver = "0.52.25"
pkgrel = 0
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
sha256 = "ef0ca9ee27850d1a5c863bb7ff9aa08096c9ed312ece9087b30f3a426828de82"
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
