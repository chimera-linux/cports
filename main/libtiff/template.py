pkgname = "libtiff"
pkgver = "4.5.1"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--enable-cxx", "--without-x"]
# otherwise it builds nothing
make_dir = "."
hostmakedepends = ["pkgconf"]
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
sha256 = "d7f38b6788e4a8f5da7940c5ac9424f494d8a79eba53d555f4a507167dca5e2b"


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


configure_gen = []
