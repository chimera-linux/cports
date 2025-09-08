pkgname = "libcdr"
pkgver = "0.1.8"
pkgrel = 5
build_style = "gnu_configure"
configure_args = ["--disable-debug"]
make_dir = "."
hostmakedepends = ["pkgconf", "automake", "slibtool"]
makedepends = ["lcms2-devel", "icu-devel", "librevenge-devel", "boost-devel"]
pkgdesc = "Corel Draw format importer library"
license = "MPL-2.0"
url = "https://wiki.documentfoundation.org/DLP/Libraries/libcdr"
source = f"http://dev-www.libreoffice.org/src/libcdr/libcdr-{pkgver}.tar.xz"
sha256 = "ced677c8300b29c91d3004bb1dddf0b99761bf5544991c26c2ee8f427e87193c"


@subpackage("libcdr-progs")
def _(self):
    return self.default_progs()


@subpackage("libcdr-devel")
def _(self):
    self.depends += ["boost-devel"]

    return self.default_devel()
