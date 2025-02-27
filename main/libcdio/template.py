pkgname = "libcdio"
pkgver = "2.1.0"
pkgrel = 2
build_style = "gnu_configure"
configure_gen = []
hostmakedepends = ["pkgconf"]
makedepends = ["ncurses-devel", "libcddb-devel", "linux-headers"]
checkdepends = ["bash"]
pkgdesc = "CD-ROM access library"
license = "GPL-3.0-or-later"
url = "https://www.gnu.org/software/libcdio"
source = f"$(GNU_SITE)/libcdio/libcdio-{pkgver}.tar.bz2"
sha256 = "8550e9589dbd594bfac93b81ecf129b1dc9d0d51e90f9696f1b2f9b2af32712b"
options = ["linkundefver"]


@subpackage("libcdio-devel")
def _(self):
    return self.default_devel()


@subpackage("libcdio-progs")
def _(self):
    return self.default_progs()
