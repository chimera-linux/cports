pkgname = "libtiff"
pkgver = "4.7.2"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--enable-cxx", "--without-x"]
# otherwise it builds nothing
make_dir = "."
hostmakedepends = [
    "automake",
    "pkgconf",
    "slibtool",
]
makedepends = [
    "jbigkit-devel",
    "libjpeg-turbo-devel",
    "xz-devel",
    "zlib-ng-compat-devel",
    "zstd-devel",
]
pkgdesc = "Library and tools for reading and writing TIFF data files"
license = "libtiff"
url = "http://libtiff.maptools.org"
source = f"http://download.osgeo.org/libtiff/tiff-{pkgver}.tar.gz"
sha256 = "672bd7d10aee4606171afb864f3570b83340f6a33e2c186dc0512f7145ffdf6a"
# triggers memcpy fortify issues in e.g. pillow/PIL tests in some vararg APIs
# options = ["!lto"]


def post_install(self):
    for f in (self.destdir / "usr/share/man/man3").glob("*.3tiff"):
        self.mv(f, f.with_suffix(".3"))

    self.install_license("LICENSE.md")


@subpackage("libtiff-devel")
def _(self):
    self.depends += makedepends
    return self.default_devel(extra=["usr/share/doc"])


@subpackage("libtiff-progs")
def _(self):
    return self.default_progs()
