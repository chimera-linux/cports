pkgname = "ijs"
_gsver = "9.55.0"
pkgver = "0.35"
pkgrel = 0
build_wrksrc = "ijs"
build_style = "gnu_configure"
configure_args = ["--enable-shared", "--enable-static"]
hostmakedepends = ["pkgconf", "automake", "libtool"]
pkgdesc = "IJS raster image transport protocol library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://www.ghostscript.com"
source = f"https://github.com/ArtifexSoftware/ghostpdl-downloads/releases/download/gs{_gsver.replace('.', '')}/ghostscript-{_gsver}.tar.xz"
sha256 = "6ee3057773646d6a2c6d117eb53a17d6752feadc513828e4322f68b7b7789ff6"
options = ["!distlicense"]


def post_install(self):
    self.rm(self.destdir / "usr/bin", recursive=True)


@subpackage("ijs-devel")
def _devel(self):
    # can't use default_devel, soname versioning is weird for this one
    return [
        "usr/include",
        "usr/lib/libijs.so",
        "usr/lib/libijs.a",
        "usr/lib/pkgconfig",
    ]
