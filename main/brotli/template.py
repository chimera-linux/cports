# update main/python-brotli alongside this
pkgname = "brotli"
pkgver = "1.2.1"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "ninja", "pkgconf"]
pkgdesc = "General-purpose lossless compression algorithm"
license = "MIT"
url = "https://github.com/google/brotli"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "98d35d11a78dc453aebb7d10c3748f3f73ff78c8267c0dc697b8631f67bf7e8f"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("brotli-devel")
def _(self):
    return self.default_devel()
