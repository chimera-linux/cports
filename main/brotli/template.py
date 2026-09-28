# update main/python-brotli alongside this
pkgname = "brotli"
pkgver = "1.2.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "ninja", "pkgconf"]
pkgdesc = "General-purpose lossless compression algorithm"
license = "MIT"
url = "https://github.com/google/brotli"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "816c96e8e8f193b40151dad7e8ff37b1221d019dbcb9c35cd3fadbfe6477dfec"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("brotli-devel")
def _(self):
    return self.default_devel()
