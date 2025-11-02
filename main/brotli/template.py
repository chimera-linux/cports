# update main/python-brotli alongside this
pkgname = "brotli"
pkgver = "1.1.0"
pkgrel = 1
build_style = "cmake"
hostmakedepends = ["cmake", "ninja", "pkgconf"]
pkgdesc = "General-purpose lossless compression algorithm"
license = "MIT"
url = "https://github.com/google/brotli"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "e720a6ca29428b803f4ad165371771f5398faba397edf6778837a18599ea13ff"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("brotli-progs")
def _(self):
    return self.default_progs()


@subpackage("brotli-devel")
def _(self):
    return self.default_devel()
