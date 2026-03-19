pkgname = "fastfloat"
pkgver = "8.2.4"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DFASTFLOAT_TEST=ON"]
hostmakedepends = ["cmake", "ninja"]
pkgdesc = "Library for C++ number parsing"
license = "MIT"
url = "https://github.com/fastfloat/fast_float"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "b90b3a415e4410822f50c70bd4485cf2c5e6962c2b05cf0dc88045d8af959ccc"


def post_install(self):
    self.install_license("LICENSE-MIT")
