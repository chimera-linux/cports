pkgname = "libtiff"
pkgver = "4.6.0"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--enable-cxx", "--without-x"]
make_cmd = "gmake"
# otherwise it builds nothing
make_dir = "."
hostmakedepends = [
    "automake",
    "gmake",
    "libtool",
    "pkgconf",
]
makedepends = [
    "jbigkit-devel",
    "libjpeg-turbo-devel",
    "xz-devel",
    "zstd-devel",
    "zlib-devel",
]
pkgdesc = "Library and tools for reading and writing TIFF data files"
maintainer = "q66 <q66@chimera-linux.org>"
license = "libtiff"
url = "http://libtiff.maptools.org"
source = f"http://download.osgeo.org/{pkgname}/tiff-{pkgver}.tar.gz"
sha256 = "88b3979e6d5c7e32b50d7ec72fb15af724f6ab2cbf7e10880c360a77e4b5d99a"


def post_install(self):
    for f in (self.destdir / "usr/share/man/man3").glob("*.3tiff"):
        self.mv(f, f.with_suffix(".3"))

    self.install_license("LICENSE.md")


@subpackage("libtiff-devel")
def _devel(self):
    self.depends += makedepends
    return self.default_devel(extra=["usr/share/doc"])


@subpackage("libtiff-progs")
def _progs(self):
    return self.default_progs()
