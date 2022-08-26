pkgname = "libtiff"
pkgver = "4.4.0"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--enable-cxx", "--without-x"]
# otherwise it builds nothing
make_dir = "."
hostmakedepends = ["pkgconf"]
makedepends = [
    "jbigkit-devel", "libjpeg-turbo-devel", "liblzma-devel",
    "libzstd-devel", "zlib-devel"
]
pkgdesc = "Library and tools for reading and writing TIFF data files"
maintainer = "q66 <q66@chimera-linux.org>"
license = "libtiff"
url = "http://libtiff.maptools.org"
source = f"http://download.osgeo.org/{pkgname}/tiff-{pkgver}.tar.gz"
sha256 = "917223b37538959aca3b790d2d73aa6e626b688e02dcda272aec24c2f498abed"

def post_install(self):
    for f in (self.destdir / "usr/share/man/man3").glob("*.3tiff"):
        self.mv(f, f.with_suffix(".3"))

    self.install_license("COPYRIGHT")

@subpackage("libtiff-devel")
def _devel(self):
    self.depends += makedepends
    return self.default_devel(extra = ["usr/share/doc"])

@subpackage("libtiff-progs")
def _progs(self):
    return self.default_progs()
