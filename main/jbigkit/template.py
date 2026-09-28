pkgname = "jbigkit"
pkgver = "2.2"
pkgrel = 0
build_style = "gnu_configure"
make_dir = "."
hostmakedepends = ["pkgconf", "automake", "libtool"]
checkdepends = ["check-devel"]
pkgdesc = "JBIG1 data compression standard implementation"
license = "GPL-2.0-only"
url = "http://www.cl.cam.ac.uk/~mgk25/jbigkit"
source = (
    f"https://github.com/void-linux/jbigkit-shared/archive/v{pkgver}.tar.gz"
)
sha256 = "5cccbfb3bd7daf224a244ce0578dbcf706e4f39962426ceede873262b29b9931"


def post_install(self):
    self.install_file("jbigkit.pc", "usr/lib/pkgconfig")
    self.install_file("jbigkit85.pc", "usr/lib/pkgconfig")


@subpackage("jbigkit-devel")
def _(self):
    return self.default_devel()


@subpackage("jbigkit-libs")
def _(self):
    return self.default_libs()
