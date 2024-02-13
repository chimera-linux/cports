pkgname = "motif"
pkgver = "2.3.8"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--disable-demos"]
make_dir = "."
hostmakedepends = [
    "automake",
    "flex",
    "libtool",
    "pkgconf",
]
makedepends = [
    "libxft-devel",
    "libxmu-devel",
    "libxt-devel",
    "xbitmaps",
]
pkgdesc = "Ancient X11 toolkit"
maintainer = "miko <mikoxyzzz@gmail.com>"
license = "LGPL-2.1-or-later"
url = "https://sourceforge.net/projects/motif"
source = f"{url}/files/Motif%20{pkgver}%20Source%20Code/motif-{pkgver}.tar.gz"
sha256 = "859b723666eeac7df018209d66045c9853b50b4218cecadb794e2359619ebce7"
# no tests
options = ["!check"]


# autoreconf needs these files in the src dir for whatever reason
def do_prepare(self):
    self.do("touch", "AUTHORS", "NEWS")


@subpackage("motif-devel")
def _devel(self):
    return self.default_devel()


@subpackage("motif-progs")
def _progs(self):
    return self.default_progs()
