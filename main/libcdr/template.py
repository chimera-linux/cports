pkgname = "libcdr"
pkgver = "0.1.9"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--disable-debug"]
make_dir = "."
hostmakedepends = ["pkgconf", "automake", "slibtool"]
makedepends = ["lcms2-devel", "icu-devel", "librevenge-devel", "boost-devel"]
pkgdesc = "Corel Draw format importer library"
license = "MPL-2.0"
url = "https://wiki.documentfoundation.org/DLP/Libraries/libcdr"
source = f"http://dev-www.libreoffice.org/src/libcdr/libcdr-{pkgver}.tar.xz"
sha256 = "f7bb6abdd7f226820f288a93dd8d07759833c0250d9e202af90f9b312c4665a3"


@subpackage("libcdr-progs")
def _(self):
    return self.default_progs()


@subpackage("libcdr-devel")
def _(self):
    self.depends += ["boost-devel"]

    return self.default_devel()
